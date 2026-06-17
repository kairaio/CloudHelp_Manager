#!/bin/bash

echo "🔄 Sync with remote..."
git pull origin main --rebase

echo "📦 Adding changes..."
git add .

echo "📝 Committing..."
git commit -m "auto update 🚀" || echo "✅ No changes to commit"

echo "🚀 Pushing to GitHub..."
git push origin main

echo "✅ Deployment triggered on Railway!"
