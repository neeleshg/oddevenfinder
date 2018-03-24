FROM ubuntu:latest
MAINTAINER ngurjar@neeleshgurjar.co.in

RUN apt-get update -y && apt-get install python git -y && git clone https://github.com/neeleshg/oddevenfinder.git -b development /opt/oddevenfinder && chmod 777 /opt/oddevenfinder/oddevenfinder.py

ENTRYPOINT ["/opt/oddevenfinder/oddevenfinder.py"]
