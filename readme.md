This is a usual site where the user can read news and leave comments (after registration)

### Installation process

<pre>
mkdir web_site && cd web_site && \
git clone https://github.com/annexol/sports-site.git
</pre>

After opening the project(web_site) you need to run the commands in the terminal

<pre>
pip install -r requirements.txt
cd firstsite
manage.py make migrations
manage.py make migrate
manage.py runserver
</pre>