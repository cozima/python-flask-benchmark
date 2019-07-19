# python-flask-benchmark

### local
```
$ scp -i ~/.ssh/hoge.pem * ec2-user@XX.XX.YY.ZZ:~
```
### ec2
```
$ sudo amazon-linux-extras install python3
$ sudo pip3 install --upgrade pip
$ sudo pip3 install flask
$ sudo pip3 install msgpack
$ sudo pip3 install boto3
$ sudo yum groupinstall "Development Tools"
$ sudo yum install -y python3-devel
$ sudo pip3 install uwsgi
$ sudo /usr/local/bin/uwsgi --yaml uwsgi.yml
```
