CREATE TABLE detections (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    camera_id VARCHAR,
    person_id INT,
    gender VARCHAR,
    location GEOGRAPHY(POINT, 4326)
);
