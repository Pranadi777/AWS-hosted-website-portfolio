
    # {
    #     'custom_id': ###,
    #     'title': '###',
    #     'goal': '###',
    #     'method': '###',
    #     'result': '###',
    #     'image': '###',
    #     'items': [#,#]
    #     'links': [#,#]
    # },

    # {
    #     'custom_id': ###,
    #     'name':'###',
    #     'description': '###',
    #     'url':'###'
    # },

    # {
    #     'custom_id': ###,
    #     'name':'###',
    #     'description': '###',
    #     'url':'###'
    # },

links = [
    {
        'custom_id': 101,
        'name':'Website',
        'description': 'website url for jobgenome',
        'url':'https://jobgenome.bio/'
    },
    {
        'custom_id': 102,
        'name':'Github Repo',
        'description': 'The Github repo for JobGenome',
        'url':'https://github.com/Pranadi777/JG2'
    },
    {
        'custom_id': 201,
        'name':'Github Repo',
        'description': 'The Github repo for the porfolio website',
        'url':'https://github.com/Pranadi777/website-portfolio'
    },
    {
        'custom_id': 301,
        'name':'Guru/NotumNB Demo',
        'description': 'Youtube video of website',
        'url':'https://youtu.be/tA7CL0-acjo?si=6iz5VujlQ5CFgURK'
    },
    {
        'custom_id': 302,
        'name':'Tableau Client UI/UX demo',
        'description': 'Tableau demo',
        'url':'https://youtu.be/_-LkSBuLJOQ?si=AcWFD3dk4Cj9bv7t'
    },
    {
        'custom_id': 401,
        'name':'Github Repo',
        'description': 'API developement in Django and React/Next.js',
        'url':'https://github.com/Pranadi777/Django-API-Development'
    },
    {
        'custom_id': 501,
        'name':'Github Repo',
        'description': 'Github Repo for AWS Project',
        'url':'https://github.com/Pranadi777/AWS-hosting-WordPress'
    },
    {
        'custom_id': 601,
        'name':'Github Repo',
        'description': 'Give Girdin repo',
        'url':'https://github.com/Pranadi777/RNAseq-GIV-Girdin-Study'
    },
    {
        'custom_id': 602,
        'name':'E-cig Publication',
        'description': 'Ecig publication',
        'url':'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7841355/'
    },
    {
        'custom_id': 603,
        'name':'Giv-Girdin Publication',
        'description': 'Giv Girdin publication',
        'url':'https://pubmed.ncbi.nlm.nih.gov/33055214/'
    },
    {
        'custom_id': 701,
        'name':'Github Repo, game#1',
        'description': 'Github repo for unity games',
        'url':'https://github.com/Pranadi777/dungeon-crawler-game'
    },
    {
        'custom_id': 702,
        'name':'Github Repo, game#2',
        'description': 'Github repo for unity games',
        'url':'https://github.com/Pranadi777/League-of-Legends-Trainer'
    },
    {
        'custom_id': 901,
        'name':'Dockerhub Image Repo',
        'description': 'Public Docker Repo for image',
        'url':'https://hub.docker.com/r/rpranadi/techmax-as'
    },

]

# 101 python       201 Bootstrap   301 ASG        401 PostgreSQL   501 AWS             601 Linux
# 102 bash         202 Django      302 EC2        402 MongoDB      502 Digitalocean    602 Google Analytics
# 103 C#           203 HTMX        303 EFS        403 SQlite       503 Nginx           603 Tableau
# 104 CSS          204 React       304 RDS        404 MS Access    504 Gunicorn        604 WordPress
# 105 HTML         205 Nextjs      305 Route 53   405 mysql        505 Github          605 DjangoNinja
# 106 JAVA                         306 VPC                         506 Terraform
# 107 jQuery                       307 EBS                         507 CICD
# 108 JavaScript                   308 S3                          508 Docker
# 109 R                            309 Codebuilder
# 110 VBA                        


projects = [
    {
        'custom_id': 1,
        'title': 'JobGenome.bio',
        'goal': 'Create a comprehensive life science job board with a simple a quick search feature to quickly scan new positions',
        'method': 'Scrape the web (efficiently and effectively) utilized Python libraries like Selenium, asyncio, and multi threading. Allow job seekers to search for jobs on a Django app.',
        'result': 'Scraping results in over >20,000 jobs from >300 companies, 15% of which are not on LinkedIn or Indeed',
        'image': 'jobgenome.png',
        'items': [101,104,105,107,108,201,202,203,401,403,502,503,504,601,602],
        'links': [101]
    },
    {
        'custom_id': 2,
        'title': 'Portfolio Website',
        'goal': 'Showcase projects and skills on Django app, hosted on AWS.',
        'method': "Create a simple Django app, with a trendy front-end (HTMX), deployed on everyone's favorite, AWS cloud.",
        'result': 'Landing a job is still TBD :).',
        'image': 'portfolio_website.png',
        'items': [101,104,105,107,108,201,202,203,501,301,302,305,306,307,307,403,601,602],
        'links': [201]
    },
    {
        'custom_id': 3,
        'title': 'NotumNB',
        'goal': 'Create app to support NotumNB functions such as: creating candidate profiles, grading assessments, and providing clients a UI/UX. Also have the front-end be usbale by non-tech people.',
        'method': 'Built a Python, MongoDB, and WordPress (friendly UI/UX).',
        'result': 'Website provided a portal for clients, candidates, and NotumNB employees to interact with.',
        'image': 'notumnb.png',
        'items': [101,402,603,604],
        'links': [301,302]
    },
    {
        'custom_id': 4,
        'title': 'API development',
        'goal': 'Learn API developement',
        'method': 'Develop an API on Django, with a React/Next.js to consume it.',
        'result': 'Built an API using Django Ninja, with a React/Next.js app that consumes it.',
        'image': 'apidev.png',
        'items': [101,104,105,108,201,202,204,205,403,605],
        'links': [401]
    },
    {
        'custom_id': 5,
        'title': 'AWS Cloud Project',
        'goal': 'Learn AWS resources by deploying an app on the cloud.',
        'method': 'AWS resources including EC2, RDS, ASG, VPC, Load balancers, and more.',
        'result': 'Deployed and hosted a highly-available WordPress application on AWS using EC2, RDS (SQL), Route 53, ASG, and VPC',
        'image': 'AWS_architecture.png',
        'items': [102,301,302,303,304,305,306,405,501,601,604],
        'links': [501]
    },
    {
        'custom_id': 6,
        'title': 'Bioinformatics and RNAseq Analysis',
        'goal': "While at UCSD's HUMANOID, become the in-house bioinformatician for RNAseq and SNP studies.",
        'method': 'R, bioinformatic libraries, and bash/shell scripting.',
        'result': 'Analyzed data for a dozen projects, resulting in a couple publications.',
        'image': 'rnaseq.png',
        'items': [109,601],
        'links': [601,602,603]
    },
    {
        'custom_id': 7,
        'title': 'Unity Game Development',
        'goal': "Play around with creating games in Unity",
        'method': 'Use the Unity game engine, coding in C#',
        'result': 'Created a couple of games including a dungeon crawler and lol skill shot trainer.',
        'image': 'Dungeon-Crawler.png',
        'items': [103],
        'links': [701,702]
    },
    {
        'custom_id': 8,
        'title': 'AWS-Continuous Integration and Continuous Deployment (CICD) of an app on AWS using Terraform, AWS CodeBuild, and Github',
        'goal': "Learn the basics of CI/CD, Terraform, S3, and CodeBuild",
        'method': 'See skills below',
        'result': 'Created an app that was continously integrated and depployed via on Github commits, Terraform, AWS CodeBuild, and S3',
        'image': 'cicd_terraform.png',
        'items': [501,302,306,308,309,505,506,507,601],
        'links': []
    },
    {
        'custom_id': 9,
        'title': 'Automating Docker Image Building using AWS Codebuild',
        'goal': "Learn the basics of building Docker images and automating the process using AWS Codebuild",
        'method': 'See skills below',
        'result': 'Codebuild job that automatically builds a Docker image and pushes it to Dockerhub.',
        'image': 'codebuild_docker.png',
        'items': [501,309,505,507,508,601],
        'links': [901]
    },
]

# 101 python       201 Bootstrap   301 ASG        401 PostgreSQL   501 AWS             601 Linux
# 102 bash         202 Django      302 EC2        402 MongoDB      502 Digitalocean    602 Google Analytics
# 103 C#           203 HTMX        303 EFS        403 SQlite       503 Nginx           603 Tableau
# 104 CSS          204 React       304 RDS        404 MS Access    504 Gunicorn        604 WordPress
# 105 HTML         205 Nextjs      305 Route 53   405 mysql        505 Github          605 DjangoNinja
# 106 JAVA                         306 VPC                         506 Terraform
# 107 jQuery                       307 EBS                         507 CICD
# 108 JavaScript                   308 S3                          508 Docker
# 109 R                            309 Codebuilder
# 110 VBA       

items = [
    {
        'custom_id' : 101,
        'name': 'Python',
        'reference': 'python',
        'type':'language',
        'image': 'python.png',
    },
    {
        'custom_id' : 102,
        'name': 'Bash',
        'reference': 'bash',
        'type':'language',
        'image': 'bash.png',
    },
    {
        'custom_id' : 103,
        'name': 'C#',
        'reference': 'c_sharp',
        'type':'language',
        'image': 'c_sharp.png',
    },
    {
        'custom_id' : 104,
        'name': 'CSS',
        'reference': 'css',
        'type':'language',
        'image': 'css.png',
    },
    {
        'custom_id' : 105,
        'name': 'HTML',
        'reference': 'html',
        'type':'language',
        'image': 'html.png',
    },
    {
        'custom_id' : 106,
        'name': 'Java',
        'reference': 'java',
        'type':'language',
        'image': 'java.png',
    },
    {
        'custom_id' : 107,
        'name': 'jQuery',
        'reference': 'jquery',
        'type':'language',
        'image': 'jquery.png',
    },
    {
        'custom_id' : 108,
        'name': 'JavaScript',
        'reference': 'js',
        'type':'language',
        'image': 'js.png',
    },
    {
        'custom_id' : 109,
        'name': 'R',
        'reference': 'r',
        'type':'language',
        'image': 'r.png',
    },
    {
        'custom_id' : 110,
        'name': 'VBA',
        'reference': 'vba',
        'type':'language',
        'image': 'vba.png',
    },
    {
        'custom_id' : 201,
        'name': 'Bootstrap',
        'reference': 'bootstrap',
        'type':'framework',
        'image': 'bootstrap.png',
    },
    {
        'custom_id' : 202,
        'name': 'Django',
        'reference': 'django',
        'type':'framework',
        'image': 'django.png',
        
    },
    {
        'custom_id' : 203,
        'name': 'HTMX',
        'reference': 'htmx',
        'type':'framework',
        'image': 'htmx.png',
    },
    {
        'custom_id' : 204,
        'name': 'React',
        'reference': 'react',
        'type':'framework',
        'image': 'react.png',
    },
    {
        'custom_id' : 205,
        'name': 'Next.js',
        'reference': 'nextjs',
        'type':'framework',
        'image': 'nextjs.png',
    },
    {
        'custom_id' : 301,
        'name': 'ASG',
        'reference': 'asg',
        'type':'aws',
        'image': 'asg.svg',
    },
    {
        'custom_id' : 302,
        'name': 'EC2',
        'reference': 'ec2',
        'type':'aws',
        'image': 'ec2.svg',
    },
    {
        'custom_id' : 303,
        'name': 'EFS',
        'reference': 'efs',
        'type':'aws',
        'image': 'efs.svg',
    },
    {
        'custom_id' : 304,
        'name': 'RDS',
        'reference': 'rds',
        'type':'aws',
        'image': 'rds.svg',
    },
    {
        'custom_id' : 305,
        'name': 'Route 53',
        'reference': 'route_53',
        'type':'aws',
        'image': 'route_53.svg',
    },
    {
        'custom_id' : 306,
        'name': 'VPC',
        'reference': 'vpc',
        'type':'aws',
        'image': 'vpc.svg',
    },
    {
        'custom_id' : 307,
        'name': 'EBS',
        'reference': 'ebs',
        'type':'aws',
        'image': 'ebs.svg',
    },
    {
        'custom_id' : 308,
        'name': 'S3',
        'reference': 's3',
        'type':'aws',
        'image': 's3.svg',
    },
    {
        'custom_id' : 309,
        'name': 'CodeBuild',
        'reference': 'codebuild',
        'type':'aws',
        'image': 'codebuild.svg',
    },
    {
        'custom_id' : 401,
        'name': 'PostgreSQL',
        'reference': 'postgresql',
        'type':'database',
        'image': 'postgresql.png',
    },
    {
        'custom_id' : 402,
        'name': 'MongoDB',
        'reference': 'mongodb',
        'type':'database',
        'image': 'mongodb.png',
    },
    {
        'custom_id' : 403,
        'name': 'SQlite',
        'reference': 'sqlite',
        'type':'database',
        'image': 'sqlite.png',
    },
    {
        'custom_id' : 404,
        'name': 'MS Access',
        'reference': 'msaccess',
        'type':'database',
        'image': 'msaccess.png',
    },
    {
        'custom_id' : 405,
        'name': 'MySQL',
        'reference': 'mysql',
        'type':'database',
        'image': 'mysql.png',
    },
    {
        'custom_id' : 501,
        'name': 'AWS',
        'reference': 'aws',
        'type':'hosting',
        'image': 'aws.png',
    },
    {
        'custom_id' : 502,
        'name': 'Digital Ocean',
        'reference': 'digitalocean',
        'type':'hosting',
        'image': 'digitalocean.png',
    },
    {
        'custom_id' : 503,
        'name': 'Nginx',
        'reference': 'nginx',
        'type':'hosting',
        'image': 'nginx.png',
    },
    {
        'custom_id' : 504,
        'name': 'Gunicorn',
        'reference': 'gunicorn',
        'type':'hosting',
        'image': 'gunicorn.png',
    },
    {
        'custom_id' : 505,
        'name': 'Github',
        'reference': 'github',
        'type':'hosting',
        'image': 'github.svg',
    },
    {
        'custom_id' : 506,
        'name': 'Terraform',
        'reference': 'terraform',
        'type':'hosting',
        'image': 'terraform.svg',
    },
    {
        'custom_id' : 507,
        'name': 'CI/CD',
        'reference': 'cicd',
        'type':'hosting',
        'image': 'cicd.png',
    },
    {
        'custom_id' : 508,
        'name': 'Docker',
        'reference': 'docker',
        'type':'hosting',
        'image': 'docker.svg',
    },
    {
        'custom_id' : 601,
        'name': 'Linux',
        'reference': 'linux',
        'type':'other',
        'image': 'linux.png',
    },
    {
        'custom_id' : 602,
        'name': 'Google Analytics',
        'reference': 'googleanalytics',
        'type':'other',
        'image': 'googleanalytics.png',
    },
    {
        'custom_id' : 603,
        'name': 'Tableau',
        'reference': 'tableau',
        'type':'other',
        'image': 'tableau.png',
    },
    {
        'custom_id' : 604,
        'name': 'Wordpress',
        'reference': 'wordpress',
        'type':'other',
        'image': 'wordpress.png',
    },
    {
        'custom_id' : 605,
        'name': 'Django Ninja',
        'reference': 'djangoninja',
        'type':'other',
        'image': 'djangoninja.png',
    },

]