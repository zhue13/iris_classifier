#Script for running bash commands that build image and run container

echo "Building image: "
docker build -t iris .

echo "Running container: "
docker run --rm -it iris
