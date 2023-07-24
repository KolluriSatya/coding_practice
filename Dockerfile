FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY environment.yml .

RUN conda env create -f environment.yml

# Override default shell and use bash
SHELL ["conda", "run", "-n", "evergreen", "/bin/bash", "-c"]

RUN kma -h

RUN conda activate evergreen

ENTRYPOINT ["conda", "run", "-n", "evergreen"]
