# GitHub Repository Setup

## Quick Setup (5 minutes)

### Step 1: Create Repository on GitHub
1. Go to https://github.com/new
2. **Repository name:** `god-mode`
3. **Description:** `Asymmetric Semantic Compression for Large-Scale AI Agents - 90% cost reduction, 4.4× lower latency`
4. **Public** (required for arXiv linking)
5. **Do NOT initialize** with README, gitignore, or license (we already have these)
6. Click "Create repository"

### Step 2: Push Local Repository
GitHub will show you commands. Use these:

```bash
cd /home/gnufoo/clawd/projects/semantic-cipher

# Add remote
git remote add origin https://github.com/YOUR_USERNAME/god-mode.git

# Push
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME`** with your GitHub username.

### Step 3: Verify
Check https://github.com/YOUR_USERNAME/god-mode - you should see all files.

---

## What's Already Ready

✅ Local git repo initialized
✅ All files committed (22 files, 6,674 lines)
✅ Clean structure:
   - README.md (professional homepage)
   - LICENSE (MIT)
   - Paper (god-mode.tex, refs.bib)
   - Code (engine.py, test_god_model.py)
   - Docs (all markdown guides)

---

## After Pushing

Update README with your actual GitHub username:
```bash
cd /home/gnufoo/clawd/projects/semantic-cipher
sed -i 's/vectorlabs/YOUR_USERNAME/g' README.md
git add README.md
git commit -m "Update GitHub URLs"
git push
```

---

## Alternative: Use GitHub CLI

If you have `gh` CLI configured:
```bash
cd /home/gnufoo/clawd/projects/semantic-cipher
gh repo create god-mode --public --source=. --remote=origin --push
```

Done in one command!

---

**Current status:** Local repo ready at `/home/gnufoo/clawd/projects/semantic-cipher/`
**Next step:** Create remote repo on GitHub and push
