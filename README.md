# Automatic Resume

A clean, automated LaTeX-based resume/CV template with multi-format output and a simple website. This project enables you to maintain your resume in LaTeX, automatically generate PDF and HTML versions, and publish them online with ease.

## Features

- **LaTeX Resume Template**: Professionally designed, clean, and modern template with sections for Work Experience, Education, Projects, Certifications, and Technical Skills.
- **Multi-format Output**: Generates both PDF and HTML versions of your resume.
- **Publication List**: Supports BibTeX (`citations.bib`) for listing academic publications.
- **Font Awesome Integration**: Uses Font Awesome icons for contact and social links.
- **Automated Image Replacement**: Python script (`replace_images.py`) to swap placeholder images with Font Awesome icons in the HTML output.
- **Website Integration**: Simple static site (`website/index.html`) to showcase your resume online.
- **Resume Variants**: Maintain different resume versions for Java, JavaScript, and Python roles under `ResumeVariants/`.
- **GitHub Actions Ready**: Designed for CI/CD workflows to auto-publish the latest resume to GitHub Pages or other static hosts.

## Project Structure

```
/Automatic-resume
│
├── Neeraj_Butola_Resume.tex         # Main LaTeX resume source
├── citations.bib                    # BibTeX file for publications
├── addfascript.py                   # (Commented) script for HTML manipulation
├── replace_images.py                # Script to replace images with icons in HTML
├── github_artifacts/                # Output directory for generated PDFs
│   └── Neeraj_Butola_Resume.pdf
├── ResumeVariants/                  # Resume variants for different roles
│   ├── Java/Neeraj_Butola_Resume.tex
│   ├── javascript/Neeraj_Butola_Resume.tex
│   └── Python/Neeraj_Butola_Resume.tex
└── website/
    ├── index.html                   # HTML version of the resume
    └── package.json                 # (Optional) for future web enhancements
```

## Usage

### 1. Edit Your Resume

- Update `Neeraj_Butola_Resume.tex` with your latest information.
- Add publications to `citations.bib` if needed.
- For different job roles, edit the corresponding file in `ResumeVariants/`.

### 2. Compile LaTeX to PDF/HTML

- Use your preferred LaTeX editor or run:
  ```sh
  pdflatex Neeraj_Butola_Resume.tex
  ```
- To generate HTML (requires TeX4ht or similar):
  ```sh
  htlatex Neeraj_Butola_Resume.tex
  ```

### 3. Enhance HTML Output

- Run the image replacement script to swap placeholder images with Font Awesome icons:
  ```sh
  python3 replace_images.py
  ```

### 4. Publish Online

- Place the generated PDF and HTML in the `website/` or `github_artifacts/` directory.
- Deploy the `website/` folder to GitHub Pages or Netlify for a live online resume.

### 5. Automation (Optional)

- Set up a GitHub Action to auto-compile and publish your resume on every push.
- Configure GitHub Pages to serve from the `website/` or `build/` directory.

## Example

- [Live Resume Demo](https://neerajbutola.netlify.app)
- [PDF Resume](github_artifacts/Neeraj_Butola_Resume.pdf)

## Scripts

- `replace_images.py`: Replaces specific image tags in the HTML with Font Awesome icons for a modern look.
- `addfascript.py`: (Commented) Example script for further HTML manipulation using BeautifulSoup.

## License

This project is open source and available under the MIT License.
