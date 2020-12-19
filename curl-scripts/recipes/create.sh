#!/bin/bash

curl "http://localhost:8000/recipes/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "recipe": {
      "title": "'"${TITLE}"'",
      "description": "'"${DESCRIPTION}"'",
      "cuisine": "'"${CUISINE}"'",
      "ingredients": "'"${INGREDIENTS}"'"
      "instructions": "'"${INSTRUCTIONS}"'",
    }
  }'

echo
