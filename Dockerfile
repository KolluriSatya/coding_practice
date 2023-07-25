FROM continuumio/miniconda3

WORKDIR /scripts

# Create the environment:
COPY environment.yml .
RUN pip freeze > environment.yml
RUN conda env create --file environment.yml

# Override default shell and use bash
SHELL ["conda", "run", "-n", "evergreen", "/bin/bash", "-c"]

RUN kma -h

RUN conda activate evergreen

ENTRYPOINT ["conda", "run", "-n", "evergreen"]
