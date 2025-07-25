import re

# Original text message
text = """
1515 Pacific Ave, Los Angeles, CA 90291, United States
(541) 754-3010 · email@email.com
MICHELLE LOPEZ, Fashion Designer
Expert Fashion Designer with 11+ years’ experience in women’s 
high-end shoes. Launched product lines for Chanel and Gucci. 
Designs showcased in Elle and Vogue. Attained recognition of 
top seller fashionista in 2017.
Details
Nationality
American
Place of birth
San Antonio
Driving license
Full
Employment History
Senior Fashion Designer  at Escada, Milan
January 2017 — July 2021
Functioned as the lead designer for the 2019 women’s winter collection team and supervised 
seasonal conceptualization and design of women’s accessories, which included belts and 
bags.
• Designed attractive fashion items that coincided with the brand’s look.
• Ran the whole product design process, from primary market research, mood board 
development to sketching and design to producing the finished product.
• Contributed to the conceptual development of directional product lines, which included 
delivering original concept pitches.
• Supervised technical designs of all products from concept design to manufacturing, 
including trim and fabric selection, meeting and choosing from vendors, etc.
Associate Fashion Designer at Dior Homme, New York
January 2014 — December 2018
Produced commercial designs are reflecting the abstract direction and business strategy of 
the company.
• Created seasonal products which focused on style, fabric, and fit.
• Leveraged processes to predict customers’ needs in order to surpass customer 
expectations and react punctually to their requirements.
• Developed and upheld effective relations with eight vital partners.
• Worked together and followed up with vendors regarding deliverables and 
main partners throughout the whole design process, including preproduction, 
merchandising, and product development.
Education
Bachelor of Arts in Fashion Design, University of Illinois , Chicago
July 2019 — Present
• 2nd place for Best Uniform Design at the Yearly Gallant Show for 2014
• Major subjects included Design Theory CAD and advanced level
• Dissertation on topic “Evolution of faux leather and high ankle boots.”
• Designed clothesline for university sports personnel
Adobe Certified Expert, Adobe, Online
July 2021 — Present
• Course Topics: Illustrator & Photoshop
Associates Degree in Fashion Design, University of Southern California, 
San Jacinto
January 2015 — June 2017
Links
LinkedIn
Resume Templates
Pinterest
Build this template
Skills
Adobe Illustrator
Hand Drafting
Fabric
Fashion Design
Design Patterns
Accomplishments
• Developed a men’s winter collection renowned by Vogue’s and Marie Claire’s editorial 
teams for its Art Nouveau style. The collection became a commercial success, boosting 
sales numbers by 46%.
• Created a highly admired women’s summer collection that increased revenue by 38% 
compared to last year.
• Managed a team of 6 designers to create 155 SKUs each month for a children’s apparel 
company.
• Enhanced the company’s main designing platform from 6 to 4, resulting in costs-savings 
of $67,000 per SKU due to scale efficiencies.
Hobbies
Art, Rugby, Cricket
Languages
English Native speaker
Italian Native speaker
 
"""

# Cleaning the text
cleaned_text = text

# 1. Add one line space before "Experience" and correct the spelling.
cleaned_text = re.sub(r"(E\s*)xperi\s*ence", "\nExperience", cleaned_text)

# 2. Add space before "Skills" and correct the spelling.
cleaned_text = re.sub(r"(S\s*)ki\s*ll\s*s", "\nSkills", cleaned_text)

# 3. Add space before "Education" and correct the spelling.
cleaned_text = re.sub(r"(E\s*)du\s*cat\s*ion", "\nEducation", cleaned_text)

# 4. Add space before "Activities" and correct the spelling.
cleaned_text = re.sub(r"(A\s*)cti\s*vi\s*ti\s*es", "\nActivities", cleaned_text)


# Printing cleaned text
print(cleaned_text)
