FROM centos:latest
MAINTAINER pranita 
RUN yum -y install httpd
COPY index.html /var/www/html/
#/usr/sbin/httpd to start the web server
#-D forground means detach foreground and run in background
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
EXPOSE 80
