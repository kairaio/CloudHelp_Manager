#!/bin/bash

echo "📥 Pulling latest changes..."
git pull origin main --rebase

echo "📦 Adding files..."
git add .

echo "📝 Committing changes..."
git commit -m "auto push update" || echo "No changes to commit"

echo "🚀 Pushing to GitHub..."
git push origin main

echo "✅ Done!"
``