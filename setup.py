from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="naas-drivers",
    version="0.73.0",
    author="Martin Donadieu",
    author_email="martindonadieu@gmail.com",
    license="BSD",
    description="Drivers made to easy connect to any services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jupyter-naas/drivers",
    packages=find_packages(exclude=["tests"]),
    extras_require={
        "dev": [
            "pytest==6.2.3",
            "pytest-mock==3.6.0",
            "requests-mock==1.9.1",
            "twine==3.4.1",
            "flake8==3.9.1",
            "black==21.4b2",
            "commitizen==2.17.4",
            "pytest-cov==2.11.1",
        ]
    },
    install_requires=[
        "pyppeteer==0.2.5",
        "imap_tools==0.39.0",
        "slackclient==2.9.3",
        "pymsteams==0.1.14",
        "pdfkit==0.6.1",
        "markdown2==2.4.0",
        "newsapi-python==0.2.6",
        "airtable-python-wrapper==0.15.2",
        "notion==0.0.28",
        "pyjwt==2.1.0",
        "tensorflow==2.6.0",
        "pysftp==0.2.9",
        "htmlbuilder==0.1.2",
        "vaderSentiment==3.3.2",
        "chardet==4.0.0",
        "Cython==0.29.23",
        "idna==2.9",
        "inflection==0.5.1",
        "joblib==1.0.1",
        "more-itertools==8.7.0",
        "numpy==1.19.5",
        "ipython==7.22.0",
        "pandas==1.2.4",
        "pandas-datareader==0.9.0",
        "patsy==0.5.1",
        "pmdarima==1.8.2",
        "python-dateutil==2.8.1",
        "python-dotenv==0.17.0",
        "pytz==2021.1",
        "plotly==4.14.3",
        "kaleido==0.2.1",
        "Quandl==3.6.1",
        "requests==2.25.1",
        "scikit-learn==0.24.2",
        "torch==1.8.1",
        "scipy==1.6.3",
        "six==1.15.0",
        "statsmodels==0.12.2",
        "urllib3==1.26.4",
        "xlrd==2.0.1",
        "pymongo==3.11.3",
        "pysftp==0.2.9",
        "md2pdf==0.5",
        "sendgrid==6.7.0",
        "escapism==1.0.1",
        "openpyxl==3.0.7",
        "google==3.0.0",
        "google-api-python-client==2.3.0",
        "google-auth-httplib2==0.1.0",
        "google-auth-oauthlib==0.4.4",
        "gspread==3.7.0",
        "oauth2client==4.1.3",
        "geopy==2.1.0",
        "GitPython==3.1.14",
        "cson==0.8",
        "opencv-python==4.5.1.48",
        "pytesseract==0.3.7",
        "wkhtmltopdf==0.2",
        "streamlit==0.82.0",
        "transformers==4.6.1",
        "pyngrok==5.0.5",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: BSD License",
        "Framework :: Jupyter",
        "Operating System :: OS Independent",
    ],
)
