# Run Project
```
docker-compose up -d
```


## LOGIN

curl -X POST http://localhost:5000/auth/login \
     -H "Content-Type: application/json" \
     -d '{"username": "free_user", "password": "1234"}'


## AI TASK INITIATE

curl -X POST http://localhost:5000/api/ai-task \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer your_jwt_token_here" \
     -d '{}'
