# Auto-Resume

A clean CV template for a resume in LaTeX along with a GitHub action that complies the `*.tex` file and publishes a new PDF version AND HTML version of the resume  when new changes are pushed to the repo

## Template Design

The template is designed to be clean with sections for

- Tabular sections for Work Experience, Education and Projects
- Support for including a list of publications read from a `*.bib` file
- Header with Font Awesome icons

Optionally, while forking this repo, you can get a direct link to the generated PDF which you can use on your website, LinkedIn etc. that will always point to the latest version of your CV. For this, after editing your copy of `cv.tex` and pushing changes to your repo, under Settings -> Pages set your Github Pages source to the `build` directory

![](https://i.imgur.com/lwATw1o.png)

Now, once your site is published, your CV will be accessible at: https://username.github.io/autoCV/cv.pdf


