# Mistral AI Hackathon Project - LLM Fine-tuning for Sango Translation

![](presentation/MistralAI_hackathon_presentation.mp4)

## Table of Contents
1. [Project Description](#project-description)
2. [Dataset](#dataset)
3. [Model Training](#model-training)
4. [Results](#results)
5. [Next Steps](#next-steps)
6. [Resources and Licensing](#resources-and-licensing)
7. [Contact](#contact)

## Project Description
This project was developed as part of the Mistral AI fine-tuning hackathon, which took place from June 5 - 30, 2024. The primary goal was to use Mistral's fine-tuning API to build a robust translation system for Sango, the lingua franca of the Central African Republic. Sango is a language with limited online resources, and this project aims to bridge the digital language gap, empowering Sango speakers across the region, fostering education, information access, and a stronger sense of community.

## Dataset
The dataset used for this project was manually built and consists of 38,000 pairs of French-Sango translations. The sources for the dataset include:
- The French-Sango dictionary
- Personal translations
- Sentences from learning websites

Building this dataset was a time-consuming process due to the scarcity of online resources. The manual effort to compile and verify translations ensures a high level of accuracy and relevance.

## Model Training
The model was trained on the 38,000 translation pairs over 200 steps and tested on 100 example pairs taken from the FLORES-200 benchmark. Due to limited credits, the training was constrained to 200 steps. Multiple models were trained to ensure a comprehensive approach within the given resources.
The model used for fine-tuning was the `open-mistral-7b`.

## Results
The performance of the model was evaluated using several metrics. Here are the results:

- **BLEU:** 0.005
- **ROUGE-1:** 0.250
- **ROUGE-2:** 0.037
- **ROUGE-L:** 0.182
- **METEOR:** 0.076
- **TER:** 95.782

### Explanation of Results
The model shows promising results for some translations but struggles with complex sentences. The corpus lacked a wide range of sentences to help the model learn the nuances of the Sango language.

#### Example Translations:
- **Good Translation:**
  - **French:** S'il t'offre une bière, refuse-la. (If he offers you a beer, refuse it.)
  - **Result (Sango):** Mû biëre na mo, kîri nî.
  - **Expected (Sango):** Tongana lo mu samba na ala, ala ken

- **Poor Translation:**
  - **French:** Les gens l'achètent seulement. (People just buy it.)
  - **Result (Sango):** Âzo ayeke vo yê hîo hîo. (Literal: People buy it quickly.)
  - **Expected (Sango):** Azo avo gi vongo.

## Next Steps
To improve the Sango translation model, the following steps are recommended:
1. **Building a Larger Dataset:** Expanding the dataset with more diverse sentences to cover a broader spectrum of the language.
2. **Improving Data Pre-processing:** Enhancing the quality and consistency of the dataset through better pre-processing techniques.
3. **Training for Longer:** Allocating more time and resources to train the model for a longer duration to improve its learning capabilities.
4. **Fine-tuning Hyperparameters:** Experimenting with different hyperparameters to optimize the model's performance.
5. **Incorporating Feedback:** Utilizing user feedback to refine and improve the translation quality.

## Resources and Licensing
The resources used for creating the dataset are open access and can be used without restriction. The primary sources include:
- French-Sango dictionary
- Various Sango learning websites :
    - [http://centrafrique.sango.free.fr/index.php](http://centrafrique.sango.free.fr/index.php)
    - [emsome.terre.defense.gouv.fr](https://www.emsome.terre.defense.gouv.fr/images/documents/bibliotheque/prix_interculturalite/20170701_NP_CFT_EMSOME_DFSHM_PRIX-OPEX.pdf)
    - [https://japprendslesango.com/](https://japprendslesango.com/)
    - [http://sangolangue.over-blog.com/](http://sangolangue.over-blog.com/)
- Personal translations

The resources used to create the dataset are believed to be open-source and freely usable. However, if there are any licensing concerns, please contact me, and the data will be promptly removed from the training set.

## Acknowledgments
- Mistral AI for organizing the fine-tuning hackathon and providing free API access
- Contributors to the French-Sango dictionary and language learning resources
- The FLORES-200 benchmark team for providing evaluation data

## License
This project is open-source and available under [Apache 2.0](LICENSE). The training data is believed to be from open-access sources. If you identify any licensing issues, please contact the maintainer immediately.

## Contact
For any questions or concerns regarding this project, please feel free to reach out to me at [habib.adoum01@gmail.com](mailto:habib.adoum01@gmail.com)
