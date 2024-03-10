
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

]

# 101 python       201 Bootstrap   301 ASG        401 PostgreSQL   501 AWS             601 Linux
# 102 bash         202 Django      302 EC2        402 MongoDB      502 Digitalocean    602 Google Analytics
# 103 C#           203 HTMX        303 EFS        403 SQlite       503 Nginx           603 Tableau
# 104 CSS          204 React       304 RDS        404 MS Access    504 Gunicorn        604 WordPress
# 105 HTML         205 Nextjs                305 Route 53                                        605 DjangoNinja
# 106 JAVA                         306 VPC 
# 107 jQuery                       307 EBS
# 108 JavaScript                   
# 109 R                         
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
        'items': [101,104,105,107,108,201,202,203,501,307,403,601,602],
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
        'items': [101,104,105,107,108,201,202,203,204,205,307,403,605],
        'links': [401]
    },
]

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