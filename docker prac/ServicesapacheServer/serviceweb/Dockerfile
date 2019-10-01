FROM centos:latest
MAINTAINER darshan  <darshanhingu729.com>
RUN yum -y install httpd
COPY index.html /var/www/html/
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
EXPOSE 80
