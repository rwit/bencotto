import os
import argparse

def CreateSiteAB(path):
    dirs = ['db', 'log', 'pid', 'sock', 'tmp', 'test', 'uploads']
    for dir in dirs:
        p = os.path.join(path, dir)
        print p
        os.makedirs(p)
    #run virtualenv
    cmd = 'virtualenv {}'.format(path)
    print cmd
    os.system(cmd)
    
def CreateSite(args):
    siteRootPath = os.path.join(os.path.abspath(os.path.expanduser(args.path)), args.site_name)
    projectSourcePath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), args.project_name)
    
    abPaths = [
        os.path.join(siteRootPath, args.site_name + '-a'),
        os.path.join(siteRootPath, args.site_name + '-b')]
    if os.path.exists(siteRootPath):
        raise os.error(siteRootPath)
    if not os.path.exists(projectSourcePath):
        raise os.error(projectSourcePath)
    os.makedirs(siteRootPath)
    for dir in abPaths:
        CreateSiteAB(dir)
    #link the source project root to the site root
    cmd = 'ln -s {} {}'.format(projectSourcePath, os.path.join(abPaths[0], args.project_name))
    print cmd
    os.system(cmd)
    #create link from site to site-a
    cmd = 'ln -s {} {}'.format(abPaths[0], os.path.join(siteRootPath, args.site_name))
    print cmd
    os.system(cmd)
    #Tip to activate the virtualenv
    print 'To activate the virtualenv run following command: source {}/bin/activate'.format(abPaths[0])
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Creates a site root', epilog='make sure to run with the user the also runs the webserver')
    parser.add_argument('--path', required=True, help='The path to create the site root in')
    parser.add_argument('--site-name', required=True, help='Name of the site')
    parser.add_argument('--project-name', required=True, help='Name of the project')
    args = parser.parse_args()
    CreateSite(args)
