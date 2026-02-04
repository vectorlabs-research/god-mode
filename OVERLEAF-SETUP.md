# Overleaf Setup Guide for God Mode Paper

## Option 1: Direct Upload to Overleaf (Recommended)

### Step 1: Create Overleaf Project
1. Go to https://www.overleaf.com
2. Sign up/login
3. Click "New Project" → "Blank Project"
4. Name it: "god-mode-arxiv"

### Step 2: Upload Files
1. Click "Upload" icon in Overleaf
2. Upload these files from `projects/semantic-cipher/`:
   - `god-mode.tex`
   - `refs.bib`

### Step 3: Compile
1. Click "Recompile" in Overleaf
2. LaTeX will compile automatically
3. PDF will appear in the preview pane

### Step 4: Download PDF for arXiv
1. After compilation succeeds, click "Download PDF"
2. This is your submission-ready PDF

---

## Option 2: Local LaTeX Compilation

If you prefer to compile locally before uploading to arXiv:

### Install LaTeX (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install texlive-full
```

### Compile
```bash
cd /home/gnufoo/clawd/projects/semantic-cipher

# First pass
pdflatex god-mode.tex

# Process bibliography
bibtex god-mode

# Second pass (resolve references)
pdflatex god-mode.tex

# Third pass (finalize)
pdflatex god-mode.tex
```

### Output
- `god-mode.pdf` will be generated in the same directory

---

## Option 3: Overleaf Git Integration

For continuous editing with Git sync:

### Step 1: Create Overleaf Project
1. Create blank project as in Option 1

### Step 2: Get Git URL
1. In Overleaf, click "Menu" (top left)
2. Find "Git" section
3. Copy the Git URL (e.g., `https://git.overleaf.com/123abc...`)

### Step 3: Clone and Push
```bash
cd /home/gnufoo/clawd/projects/semantic-cipher

# Add Overleaf as remote
git remote add overleaf <OVERLEAF_GIT_URL>

# Push files
git add god-mode.tex refs.bib
git commit -m "Initial paper draft"
git push overleaf master
```

Now Overleaf will auto-sync with your local repo.

---

## Common LaTeX Errors and Fixes

### Error: "Undefined control sequence \\Omega"
**Fix:** Already handled - we use `$\Omega$` in math mode

### Error: "Missing $ inserted"
**Fix:** All special symbols (Ω, →, ×) are wrapped in math mode `$...$`

### Error: "Bibliography not found"
**Fix:** Ensure `refs.bib` is in the same directory as `god-mode.tex`

### Error: "Package hyperref Warning: Token not allowed"
**Fix:** Already handled - URLs use `\url{...}` command

---

## Verification Checklist

Before submitting to arXiv:

- [ ] PDF compiles without errors
- [ ] All citations resolve (no `[?]` in PDF)
- [ ] Tables render correctly
- [ ] Abstract fits on first page
- [ ] Author emails are correct
- [ ] Page count is reasonable (currently ~15 pages - good for arXiv)
- [ ] All URLs in references are clickable
- [ ] Figures (if added) display correctly

---

## Current Paper Status

**Compiled successfully?** Not yet - needs first compilation
**Page count:** ~15 pages (estimated)
**References:** 20 citations, all formatted
**Sections:** 8 main + 2 appendices (removed for brevity in LaTeX version)

---

## Next Actions

1. **Upload to Overleaf** (easiest) or **compile locally**
2. Review PDF for formatting issues
3. Once satisfied, proceed to arXiv submission
4. Keep Overleaf link handy for future revisions

---

## Overleaf Sharing

Once uploaded to Overleaf:
1. Click "Share" in top right
2. Options:
   - **Turn on link sharing** (anyone with link can view)
   - **Invite collaborators** (for co-authors)
   - **Make read-only** (for reviewers)

Tony - you can share the Overleaf link with me if you want me to review formatting before submission.

---

## Estimated Timeline

- **Upload to Overleaf:** 5 minutes
- **First compilation:** 1 minute
- **Review PDF:** 10-15 minutes
- **Minor fixes (if needed):** 10-30 minutes
- **Total:** ~30-60 minutes to submission-ready PDF

---

**Ready to proceed?** Let me know if you want me to walk you through any step or if you encounter errors.
