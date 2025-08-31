REM   בניית אימג'ים
docker build -t retriever-image -f retriever/Dockerfile retriever
docker build -t preprocessor-image -f preprocessor/Dockerfile preprocessor
docker build -t enricher-image -f enricher/Dockerfile enricher
docker build -t persister-image -f persister/Dockerfile persister
docker build -t dataretrieval-image -f data_retrieval/Dockerfile data_retrieval

REM הרצת קונטיינרים
docker run -d --name retriever retriever-image
docker run -d --name preprocessor preprocessor-image
docker run -d --name enricher enricher-image
docker run -d --name persister persister-image
docker run -d -p 8000:8000 --name dataretrieval dataretrieval-image

REM דחיפה לדוקר אהב
docker tag retriever-image yakiruzan/retriever
docker tag preprocessor-image yakiruzan/preprocessor
docker tag enricher-image yakiruzan/enricher
docker tag persister-image yakiruzan/persister
docker tag dataretrieval-image yakiruzan/dataretrieval

docker push yakiruzan/retriever
docker push yakiruzan/preprocessor
docker push yakiruzan/enricher
docker push yakiruzan/persister
docker push yakiruzan/dataretrieval
