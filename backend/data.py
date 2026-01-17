
DATA = {
    "course_specifics": {
        "B.Tech CSE": {
            "skills": ["Algorithms", "Full Stack Dev", "System Design", "Cybersecurity"],
            "tech": ["Large Language Models", "Edge Computing", "Web3/Blockchain", "Zero Trust Architecture"],
            "sources": [{"name": "Harvard CS50", "url": "https://learning.edx.org/course/course-v1:HarvardX+CS50+X/home"}, {"name": "FreeCodeCamp", "url": "https://www.freecodecamp.org/"}]
        },
        "Cybersecurity": {
            "skills": ["Ethical Hacking", "Network Security", "Cryptography", "Identity Management"],
            "tech": ["Quantum-resistant Crypto", "AI Threat Hunting", "Zero Knowledge Proofs"],
            "sources": [{"name": "TryHackMe", "url": "https://tryhackme.com/"}, {"name": "OWASP Guides", "url": "https://owasp.org/"}]
        },
        "Data Science": {
            "skills": ["Predictive Modeling", "Statistics", "Data Visualization", "SQL/NoSQL"],
            "tech": ["AutoML", "Feature Stores", "Real-time Stream Processing"],
            "sources": [{"name": "Kaggle Learn", "url": "https://www.kaggle.com/learn"}, {"name": "IBM Data Science", "url": "https://www.coursera.org/professional-certificates/ibm-data-science"}]
        },
        "B.Tech (Mech/Civil)": {
            "skills": ["AutoCAD/SolidWorks", "Structural Dynamics", "Thermodynamics", "Project Management"],
            "tech": ["Digital Twins", "4D Printing", "Smart Materials", "Sustainable Construction Tech"],
            "sources": [{"name": "Autodesk Academy", "url": "https://academy.autodesk.com/"}, {"name": "Engineering Explained", "url": "https://www.youtube.com/user/EngineeringExplained"}]
        },
        "Robotics & Automation": {
            "skills": ["ROS (Robot OS)", "Control Systems", "Machine Vision", "Hardware Interfacing"],
            "tech": ["Soft Robotics", "Collaborative Robots (Cobots)", "Swarm Intelligence"],
            "sources": [{"name": "ETH Zurich Robotics Lab", "url": "https://rsl.ethz.ch/"}, {"name": "Udacity Robotics", "url": "https://www.udacity.com/course/robotics-software-engineer--nd209"}]
        },
        "MBBS": {
            "skills": ["Clinical Diagnosis", "Anatomy", "Emergency Response", "Patient Ethics"],
            "tech": ["Robotic Surgery", "AI-assisted Prognosis", "Nanomedicine", "Personalized Genomics"],
            "sources": [{"name": "WHO Health Courses", "url": "https://openwho.org/"}, {"name": "Medscape", "url": "https://www.medscape.org/"}]
        },
        "B.Sc Biotech": {
            "skills": ["Gene Mapping", "Lab Culture", "Bio-informatics", "Fermentation Tech"],
            "tech": ["CRISPR-Cas9", "Synthetic Biology", "Bio-printing"],
            "sources": [{"name": "Nature Education", "url": "https://www.nature.com/scitable"}, {"name": "Biotech Basics (EdX)", "url": "https://www.edx.org/learn/biotechnology"}]
        },
        "B.Des": {
            "skills": ["User Experience (UX)", "Color Theory", "Prototyping", "Design Thinking"],
            "tech": ["Generative UI", "XR (Extended Reality)", "Procedural Art", "Neuro-design"],
            "sources": [{"name": "Google UX Design", "url": "https://www.coursera.org/professional-certificates/google-ux-design"}, {"name": "Behance", "url": "https://www.behance.net/"}]
        },
        "Gaming & Animation": {
            "skills": ["3D Modeling", "Rigging", "Unity/Unreal Engine", "VFX Graph"],
            "tech": ["Real-time Raytracing", "AI-driven Motion Capture", "Metaverse Dev"],
            "sources": [{"name": "Unreal Online Learning", "url": "https://dev.epicgames.com/community/learning"}, {"name": "Blender Guru", "url": "https://www.blenderguru.com/"}]
        },
        "B.Com / CA": {
            "skills": ["Financial Auditing", "Taxation Law", "SAP/ERP Management", "Corporate Governance"],
            "tech": ["Automated Auditing", "FinTech Regulation", "Decentralized Finance (DeFi)"],
            "sources": [{"name": "ICAI e-Learning", "url": "https://learning.icai.org/"}, {"name": "CFI Free Hub", "url": "https://corporatefinanceinstitute.com/"}]
        },
        "FinTech": {
            "skills": ["Blockchain Dev", "Financial Analysis", "Stripe/PayPal APIs", "Compliance Tech"],
            "tech": ["Smart Contracts", "Algorithmic Trading", "Open Banking"],
            "sources": [{"name": "FinTech Weekly", "url": "https://www.fintechweekly.com/"}, {"name": "Oxford FinTech Program", "url": "https://www.sbs.ox.ac.uk/programs/oxford-fintech-programme"}]
        },
        "Actuarial Science": {
            "skills": ["Risk Assessment", "Probability", "Pension Valuation", "Insurance Math"],
            "tech": ["InsurTech", "Catastrophic Risk AI", "Survival Analysis Models"],
            "sources": [{"name": "Institute of Actuaries", "url": "https://www.actuaries.org.uk/"}, {"name": "Be An Actuary", "url": "https://www.beanactuary.org/"}]
        },
        "BBA / MBA": {
            "skills": ["Strategic Leadership", "Data-driven Marketing", "Operations Research", "Financial Modeling"],
            "tech": ["MarTech Automation", "AI Business Intelligence", "Growth Hacking"],
            "sources": [{"name": "HubSpot Academy", "url": "https://academy.hubspot.com/"}, {"name": "Y Combinator", "url": "https://www.startupschool.org/"}]
        },
        "Mass Comm & Journalism": {
            "skills": ["Investigative Reporting", "Video Editing", "Social Media Strategy", "Copywriting"],
            "tech": ["Deepfake Detection", "Immersive News (VR)", "Automated Content Hubs"],
            "sources": [{"name": "Knight Center", "url": "https://journalismcourses.org/"}, {"name": "BBC Academy", "url": "https://www.bbc.co.uk/academy"}]
        },
        "Psychology": {
            "skills": ["Clinical Counseling", "Cognitive Assessment", "Observational Research", "Empathy"],
            "tech": ["VR Exposure Therapy", "Digital Mental Health Platforms", "Bio-feedback Monitoring"],
            "sources": [{"name": "Psychology Today", "url": "https://www.psychologytoday.com/"}, {"name": "American Psych Assoc (APA)", "url": "https://www.apa.org/"}]
        },
        "B.Sc Nursing": {
            "skills": ["Patient Care", "Medical Charting", "Surgical Assistance", "Pharmacology Basics"],
            "tech": ["Smart Patient Monitoring", "E-Healthcare Records", "Portable Diagnostic Gear"],
            "sources": [{"name": "WHO Health", "url": "https://openwho.org/"}, {"name": "NursingWorld", "url": "https://www.nursingworld.org/"}]
        }
    },
    "exams": {
        "top": [
            {"name": "JEE Mains (S1/S2)", "reg": "Nov-Mar", "exam": "Jan/Apr 2026"},
            {"name": "NEET UG", "reg": "Feb-Mar", "exam": "May 2026"},
            {"name": "KEAM", "reg": "Mar-Apr", "exam": "June 2026"},
            {"name": "CUET UG", "reg": "Feb-Mar", "exam": "May-June 2026"},
            {"name": "CUSAT CAT", "reg": "Jan-Feb", "exam": "May 2026"}
        ],
        "design": [
            {"name": "NID DAT", "reg": "Sept-Nov", "exam": "Jan 2026"},
            {"name": "NIFT Entrance", "reg": "Dec", "exam": "Feb 2026"},
            {"name": "UCEED", "reg": "Oct-Nov", "exam": "Jan 2026"}
        ],
        "law": [
            {"name": "CLAT", "reg": "July-Oct", "exam": "Dec 2025"},
            {"name": "KLEE (LLB)", "reg": "June", "exam": "Aug 2026"},
            {"name": "AILET", "reg": "Aug-Nov", "exam": "Dec 2025"},
            {"name": "LSAT-India", "reg": "Jan-May", "exam": "May 2026"}
        ],
        "commerce": [
            {"name": "CA Foundation", "reg": "Jan/July", "exam": "June/Dec"},
            {"name": "IPMAT (IIM)", "reg": "Feb-Apr", "exam": "May 2026"},
            {"name": "CMA", "reg": "Year-round", "exam": "June/Dec"}
        ],
        "management": [
            {"name": "IPMAT (Indore)", "reg": "Feb-Mar", "exam": "May 2026"},
            {"name": "JIPMAT", "reg": "Apr", "exam": "June 2026"},
            {"name": "SET (Symbiosis)", "reg": "Jan-Apr", "exam": "May 2026"}
        ],
        "architecture": [
            {"name": "NATA", "reg": "Mar-Aug", "exam": "Multiple/Monthly"},
            {"name": "JEE Paper 2", "reg": "Nov-Mar", "exam": "Jan/Apr 2026"}
        ],
        "nursing": [
            {"name": "AIIMS B.Sc Nursing", "reg": "Mar-Apr", "exam": "June 2026"},
            {"name": "KNRUHS (Kerala)", "reg": "May", "exam": "July 2026"},
            {"name": "Military Nursing (MNS)", "reg": "Feb", "exam": "Apr 2026"}
        ],
        "arts_science": [
            {"name": "CUET (UG)", "reg": "Feb-Mar", "exam": "May-June 2026"},
            {"name": "TISS BAT", "reg": "Jan-Feb", "exam": "May 2026"},
            {"name": "HSEE (IIT Madras)", "reg": "Dec-Jan", "exam": "Apr 2026"}
        ]
    },
    "questions": [
        {"text": "1. Which activity makes time fly for you?", "opts": [{"l": "Building/Repairing", "t": "R"}, {"l": "Solving Puzzles/Math", "t": "I"}, {"l": "Writing/Art", "t": "A"}, {"l": "Helping people", "t": "S"}]},
        {"text": "2. Do you prefer working with...", "opts": [{"l": "Data & Numbers", "t": "C"}, {"l": "People & Teams", "t": "S"}, {"l": "Machines & Tools", "t": "R"}, {"l": "Ideas & Theories", "t": "I"}]},
        {"text": "3. How much do you enjoy artistic pursuits?", "opts": [{"l": "Love it! (Draw/Sing)", "t": "A"}, {"l": "It's okay", "t": "S"}, {"l": "Not really", "t": "C"}, {"l": "Prefer Logic", "t": "I"}]},
        {"text": "4. Would you rather...", "opts": [{"l": "Invent new solutions", "t": "I"}, {"l": "Follow proven methods", "t": "C"}, {"l": "Sell the solution", "t": "E"}, {"l": "Build the prototype", "t": "R"}]},
        {"text": "5. Caring for others vs Solving technical problems?", "opts": [{"l": "Caring for others", "t": "S"}, {"l": "Technical problems", "t": "R"}, {"l": "Leading the team", "t": "E"}, {"l": "Analyze the cost", "t": "C"}]},
        {"text": "6. Interest in leading teams?", "opts": [{"l": "High - I love power", "t": "E"}, {"l": "Medium - If needed", "t": "S"}, {"l": "Low - Prefer solo", "t": "I"}, {"l": "Zero - Just tell me what to do", "t": "C"}]},
        {"text": "7. Do you enjoy researching facts?", "opts": [{"l": "Yes, deep dive", "t": "I"}, {"l": "Only if practical", "t": "R"}, {"l": "No, trust gut", "t": "A"}, {"l": "No, ask expert", "t": "S"}]},
        {"text": "8. Environment Preference?", "opts": [{"l": "Office / Desk", "t": "C"}, {"l": "Outdoors / Field", "t": "R"}, {"l": "Studio / Lab", "t": "I"}, {"l": "Busy Hospital / School", "t": "S"}]},
        {"text": "9. Building or repairing objects?", "opts": [{"l": "Love it", "t": "R"}, {"l": "Hate it", "t": "S"}, {"l": "Hire someone", "t": "E"}, {"l": "Read manual first", "t": "C"}]},
        {"text": "10. Interest in Sales/Customer roles?", "opts": [{"l": "High", "t": "E"}, {"l": "No, too stressful", "t": "I"}, {"l": "Maybe", "t": "S"}, {"l": "Prefer backend", "t": "R"}]},
        {"text": "11. Routine vs Variety?", "opts": [{"l": "Routine & Stability", "t": "C"}, {"l": "New challenges daily", "t": "E"}, {"l": "Creative freedom", "t": "A"}, {"l": "Physical activity", "t": "R"}]},
        {"text": "12. Writing reports or Presenting ideas?", "opts": [{"l": "Writing Reports", "t": "C"}, {"l": "Presenting Ideas", "t": "E"}, {"l": "Writing Stories", "t": "A"}, {"l": "Neither", "t": "R"}]},
        {"text": "13. Math-heavy or Verbal challenges?", "opts": [{"l": "Math/Logic", "t": "I"}, {"l": "Verbal/Communication", "t": "S"}, {"l": "Visual/Spatial", "t": "A"}, {"l": "Financial/Data", "t": "C"}]},
        {"text": "14. Drawn to Healthcare or Science?", "opts": [{"l": "Healthcare (Helping)", "t": "S"}, {"l": "Science (Research)", "t": "I"}, {"l": "Managing Hospital", "t": "E"}, {"l": "Using Med Tech", "t": "R"}]},
        {"text": "15. Strategy vs Hands-on?", "opts": [{"l": "Strategy (Big Picture)", "t": "E"}, {"l": "Hands-on (Execution)", "t": "R"}, {"l": "Planning (Details)", "t": "C"}, {"l": "Designing (Visual)", "t": "A"}]},
        {"text": "16. Others compliment your...", "opts": [{"l": "Listening skills", "t": "S"}, {"l": "Logical thinking", "t": "I"}, {"l": "Organizational skills", "t": "C"}, {"l": "Leadership", "t": "E"}]},
        {"text": "17. Recent project strength?", "opts": [{"l": "Coming up with ideas", "t": "A"}, {"l": "Making the plan", "t": "C"}, {"l": "Doing the work", "t": "R"}, {"l": "Presenting it", "t": "E"}]},
        {"text": "18. Public Speaking Proficiency?", "opts": [{"l": "Expert/Enjoy it", "t": "E"}, {"l": "Good enough", "t": "S"}, {"l": "Nervous but okay", "t": "C"}, {"l": "Avoid at all costs", "t": "R"}]},
        {"text": "19. Comfort with Tech Tools?", "opts": [{"l": "Tech Wizard", "t": "I"}, {"l": "User", "t": "C"}, {"l": "Creator", "t": "A"}, {"l": "Only basics", "t": "S"}]},
        {"text": "20. Planning or Improvising?", "opts": [{"l": "Strict Planner", "t": "C"}, {"l": "Improviser", "t": "A"}, {"l": "Strategic Adapter", "t": "E"}, {"l": "Practical Fixer", "t": "R"}]},
        {"text": "21. Analytical vs Creative?", "opts": [{"l": "Analytical", "t": "I"}, {"l": "Creative", "t": "A"}, {"l": "Both (Architect)", "t": "R"}, {"l": "Neither (Social)", "t": "S"}]},
        {"text": "22. Handling Conflict?", "opts": [{"l": "Mediator (Peace)", "t": "S"}, {"l": "Direct (Win)", "t": "E"}, {"l": "Avoidant", "t": "I"}, {"l": "Rule-based", "t": "C"}]},
        {"text": "23. Languages or Numbers?", "opts": [{"l": "Languages", "t": "S"}, {"l": "Numbers", "t": "C"}, {"l": "Code (Logic)", "t": "I"}, {"l": "Visuals", "t": "A"}]},
        {"text": "24. Learning Style?", "opts": [{"l": "Hands-on / Doing", "t": "R"}, {"l": "Reading / Research", "t": "I"}, {"l": "Discussing / Group", "t": "S"}, {"l": "Watching / Visual", "t": "A"}]},
        {"text": "25. Organization Skills?", "opts": [{"l": "Super Organized", "t": "C"}, {"l": "Messy but Creative", "t": "A"}, {"l": "delegator", "t": "E"}, {"l": "Efficient", "t": "R"}]},
        {"text": "26. Salary Expectation?", "opts": [{"l": "High - Wealth is key", "tag": "Money"}, {"l": "Medium - Comfort", "tag": "Stability"}, {"l": "Low warning - Passion first", "tag": "Passion"}]},
        {"text": "27. Work-Life Balance?", "opts": [{"l": "Strict 9-5", "tag": "Balance"}, {"l": "Workaholic for success", "tag": "Hustle"}, {"l": "Flexible", "tag": "Flex"}]},
        {"text": "28. Job Security vs Growth?", "opts": [{"l": "Security (Govt Job)", "tag": "Security"}, {"l": "Growth (Startup)", "tag": "Growth"}]},
        {"text": "29. Independent vs Team?", "opts": [{"l": "Solo Wolf", "tag": "Solo"}, {"l": "Team Player", "tag": "Team"}]},
        {"text": "30. Value Recognition?", "opts": [{"l": "I want fame/credit", "tag": "Fame"}, {"l": "Just satisfaction", "tag": "Inner"}]},
        {"text": "31. Travel Preference?", "opts": [{"l": "Love traveling", "tag": "Travel"}, {"l": "Homebody", "tag": "Local"}]},
        {"text": "32. Ethical Dilemmas?", "opts": [{"l": "Rules are rules", "tag": "Rules"}, {"l": "Outcome matters", "tag": "Outcome"}]},
        {"text": "33. Company Size?", "opts": [{"l": "Big MNC", "tag": "MNC"}, {"l": "Small Startup", "tag": "Startup"}]},
        {"text": "34. Contribution to Society?", "opts": [{"l": "Vital / NGO", "tag": "Impact"}, {"l": "Neutral", "tag": "Neutral"}]},
        {"text": "35. Flexible hours?", "opts": [{"l": "Yes please", "tag": "Flex"}, {"l": "No, fixed routine", "tag": "Fixed"}]}
    ],
    "descriptions": {
        "R": {
            "title": "Realistic (The Doer)", 
            "traits": "Detailed, Practical, Physical", 
            "courses": "B.Tech Mech, Civil, Robotics, Automation, Agriculture, Forestry, Physical Education, Sports Science, Forensic Science, Aviation, Pilot Training, Marine Engineering, Nautical Science, Petroleum Engineering, Mining, Geophysics, Horticulture, Animal Husbandry, Food Technology, Textile Engineering, Automobile Eng, Mechatronics, Industrial Design, Fire & Safety, Carpentry Tech, Electrician Certification, HVAC Tech, Plumbing Science, Welding Tech, CAD/CAM, CNC Machining, Building Construction, Surveying, Landscape Architecture, Environmental Eng, Renewable Energy Tech, Solar Tech, Wind Energy, Bio-processing, Dairy Tech, Fisheries Science, Sericulture, Poultry Science, Veterinary Tech, Wildlife Conservation, Park Management, Range Management, Tool & Die, Mold Making, Polymer Tech, Plastic Tech, Rubber Tech, Printing Tech, Packaging Tech, Fashion Tech, Leather Tech, Footwear Tech, Sound Engineering, Audio Production, Stage Management, Set Design, Cinematic Lighting, Broadcast Tech, Radio Eng, Satellite Tech, Remote Sensing, GIS Tech, Nano-materials, Ceramic Eng, Metallurgy, Casting Tech, Foundry Tech, Surface Coating, Corrosion Eng, Pipeline Eng, Irrigation Eng, Hydrology, Soil Science, Agronomy, Plant Pathology, Entomology, Farm Machinery, Precision Farming, Smart Grid Tech, Electric Vehicle Tech, Battery Tech, Fuel Cell Tech, Robotics Maintenance, Cobot Integration, Drone Pilot, Drone Repair, Subsea Engineering, Drilling Tech, Reservoir Eng, Wind Turbine Mantainence, Space Mining Tech, Deep Sea Exploration, Arctic Engineering, Geothermal Tech, Hydroponics Science, Vertical Farming, Urban Agriculture, Aquaponics, Mycology Tech, Permaculture Design, Arboriculture, Coastal Engineering, Port Engineering, Railway Engineering, Highway Engineering, Tunnel Engineering, Bridge Construction, Smart City Infrastructure", 
            "career": "Engineer, Pilot, Architect, Forester, Sports Physiologist, Forensic Expert, Merchant Mariner",
            "skills": ["CAD Design", "Structural Analysis", "Troubleshooting", "Equipment Operation"],
            "tech": ["3D Printing", "Robotic Automation", "BIM (Building Info Modeling)", "Drones"],
            "sources": ["MIT OpenCourseWare", "Autodesk Academy", "YouTube (Engineering Explained)"]
        },
        "I": {
            "title": "Investigative (The Thinker)", 
            "traits": "Analytical, Intellectual, Scientific", 
            "courses": "MBBS, B.Tech CSE, Data Science, Cybersecurity, Biotech, Astrophysics, B.Pharm, Vet Science, Bioinformatics, AI & ML, Physics, Archaeology, Genetics, Microbiology, Biochemistry, Neuroscience, Cognitive Science, Quantum Computing, Theoretical Physics, Organic Chemistry, Analytical Chem, Nanotechnology, Marine Biology, Ecology, Zoology, Botany, Psychology Research, Anthropology, Sociology Research, Economics (Quant), Actuarial Science, Statistics, Mathematics, Operational Research, Epidemiology, Public Health Science, Virology, Immunology, Pathology, Radiology, Oncology, Cardiology, Neurology, Genomics, Proteomics, Metabolomics, Systems Biology, Toxicology, Pharmacology, Medicinal Chemistry, Pharmacognosy, Clinical Research, Stem Cell Research, Regenerative Medicine, Tissue Engineering, Bio-materials, Biophysics, Bio-mechanics, Bio-electronics, Medical Imaging, Diagnostic Tech, Nuclear Medicine, Forensic Tech, Criminology, Paleontology, Geology, Seismology, Meteorology, Oceanography, Climatology, Space Science, Planetary Science, Astro-biology, High Energy Physics, Particle Physics, Fluid Dynamics, Material Science, Polymer Science, Computational Chemistry, Molecular Biology, Cell Biology, Endocrinology, Neuropsychology, Psychopharmacology, Experimental Psych, Behavioral Science, Data Analytics, Business Intelligence, Cryptography, Blockchain Theory, Graph Theory, Number Theory, Chaos Theory, Game Theory, String Theory, Cosmology, Paleobotany, Palynology, Volcanology, Glaciology, Limnology, Mycology, Parasitology, Entomology, Ichthyology, Herpetology, Ornithology, Mammalogy, Ethology, Evolutionary Biology, Sociobiology, Population Genetics, Bioinformatics, Computational Neuroscience, Synthetic Biology, Bionics, Nano-biotechnology, Quantum Biology, Astro-chemistry, Geochemistry, Biogeochemistry, Environmental Toxicology, Epidemiological Modeling, Biostatistics", 
            "career": "Scientist, Doctor, Software Dev, Researcher, Astronomer, Vet, Cybersecurity Analyst",
            "skills": ["Data Analysis", "Critical Thinking", "Scientific Research", "Programming"],
            "tech": ["AI & Machine Learning", "Quantum Computing", "CRISPR Gene Editing", "Big Data Analytics"],
            "sources": ["Khan Academy", "Coursera (Free Audit)", "Stanford Online", "edX"]
        },
        "A": {
            "title": "Artistic (The Creator)", 
            "traits": "Expressive, Original, Independent", 
            "courses": "B.Des, Gaming & Animation, Interior Design, Fashion Design, Film Studies, Journalism, Mass Comm, Creative Writing, Fine Arts, Sound Engineering, VFX Design, Graphic Design, Web Design, UX/UI Design, Product Design, Industrial Art, Sculpture, Painting, Printmaking, Photography, Cinematography, Animation 3D, Motion Graphics, Illustration, Comic Art, Concept Art, Storyboarding, Scriptwriting, Playwriting, Poetry, Comparative Literature, Linguistics, Music Theory, Music Composition, Vocal Performance, Instrumental Music, Jazz Studies, Electronic Music, Music Production, Dance Science, Choreography, Theatre Arts, Drama, Acting, Directing, Set Design, Costume Design, Make-up Art, Hair Styling (Creative), Jewelry Design, Ceramic Art, Glass Blowing, Textile Design, Accessory Design, Exhibition Design, Lighting Design, Acoustic Design, Digital Art, Media Arts, Interactive Media, Virtual Reality Content, Augmented Reality Design, Transmedia Storytelling, Cultural Studies, Art History, Museum Studies, Curatorial Practice, Heritage Conservation, Calligraphy, Typographic Design, Brand Identity, Advertising Art, Copywriting, Social Media Content, Podcasting, Video Production, Documentary Filmmaking, Broadcast Journalism, PR & Creative Strategy, Design Management, Sustainable Design, Social Innovation Design, Craft Science, Woodworking Art, Metal Smithing, Architectural Visualization, Character Design, Environment Art, Game Level Design, VR Experience Design, Generative Art Design, AI Art Curation, Metaverse Architecture, Digital Fashion Design, Wearable Tech Aesthetics, Soundscape Design, Foley Art, Voice Acting, Screenwriting, Travel Writing, Food Styling, Makeup FX (Prosthetics), Tattoo Art, Mural Painting, Installation Art, Performance Art, Puppetry, Magic & Illusion Arts, Circus Arts, Culinary Arts (Creative), Pastry Arts, Oenology (Art of Wine), Perfumery", 
            "career": "Designer, Writer, Filmmaker, Musician, Editor, Illustrator, Animator",
            "skills": ["Visual Design", "Creative Writing", "Storyboarding", "UX/UI Design"],
            "tech": ["Generative AI Art", "AR/VR Design", "Digital Twins", "NFTs & Digital Ownership"],
            "sources": ["Behance", "Adobe Creative Cloud Tutorials", "Google UX Design (Coursera)", "Skillshare (Free trial)"]
        },
        "S": {
            "title": "Social (The Helper)", 
            "traits": "Cooperative, Supporting, Empathetic", 
            "courses": "B.Sc Nursing, Psychology, B.Ed, Physiotherapy, Sociology, BSW, Occupational Therapy, Public Health, Counseling, Speech Therapy, Human Rights Law, Special Education, Primary Education, Early Childhood Care, Montessori, Physical Therapy, Sports Therapy, Massage Therapy, Nutrition & Dietetics, Mental Health Nursing, Midwifery, Community Health, Global Health, Social Entrepreneurship, NGO Management, Youth Work, Gerontology, Disability Studies, Addiction Counseling, Family Therapy, Marriage Counseling, Career Counseling, School Psychology, Educational Psych, Clinical Psych, Health Psych, Counseling Psych, Social Policy, Human Rights, International Relations, Peace & Conflict Studies, Sustainable Development, Community Development, Rural Development, Urban Sociology, Gender Studies, Ethnic Studies, Social Work in Healthcare, Psychiatric Social Work, Child Welfare, Elder Care, Patient Advocacy, Health Education, Wellness Coaching, Life Coaching, Spiritual Counseling, Pastoral Care, Hospitality Management, Customer Service Science, Event Management, HR Management (Social), Public Relations, Disaster Management, Humanitarian Aid, Refugee Studies, Diversity & Inclusion, Non-Profit Leadership, Volunteer Management, Adult Literacy, Vocational Training, Corporate Social Responsibility, Environmental Justice, Community Organizing, Mediation, Conflict Resolution, Animal Assisted Therapy, Music Therapy, Art Therapy, Horticultural Therapy, Prison Counseling, Victimology, Human Trafficking Advocacy, Indigenous Studies, International Development, Global Health Policy, Tele-health Coordination, Community Midwifery, Palliative Care, Rehabilitation Science, Vocational Rehab, Educational Leadership, Special Needs Policy, Inclusive Education, Language Pathology, Audiology, SIGN Language, Braille Education", 
            "career": "Teacher, Nurse, Psychologist, Social Worker, Counselor, Physio, Public Health Expert",
            "skills": ["Conflict Resolution", "Counseling", "Public Speaking", "Public Health"],
            "tech": ["Telemedicine", "AI for Mental Health", "Educational Tech (EdTech)", "Bio-feedback"],
            "sources": ["WHO Open Courses", "TED Talks", "Open University", "Psychology Today"]
        },
        "E": {
            "title": "Enterprising (The Persuader)", 
            "traits": "Ambitious, Competitive, Sociable", 
            "courses": "BBA, MBA, Integrated LLB, Hotel Management, Mass Comm, Event Management, Digital Marketing, PR, Venture Capital, Entrepreneurship, Real Estate, International Business, Strategic Management, Supply Chain Mgmt, E-commerce, Marketing Research, Brand Management, Retail Management, Fashion Management, Airline & Airport Mgmt, Shipping & Logistics, Port Management, Export-Import Mgmt, Financial Management, Investment Banking, Wealth Management, Private Equity, Risk Management, Corporate Law, Intellectual Property Law, Media Law, Cyber Law, International Law, Public Administration, Political Science, Policy Analysis, Leadership Studies, Organizational Behavior, Project Management, Sales Management, Business Development, Account Management, Crisis Management, Change Management, Talent Management, Executive Coaching, Motivational Speaking, Corporate Training, Franchising, Startup Management, Innovation Management, Technology Transfer, Govt Relations, Lobbying, Political Campaigning, Speech Writing, Media Planning, Advertising Management, Customer Relationship Mgmt, Business Analytics, Predictive Analytics (Business), FinTech Management, InsurTech Management, PropTech Management, EdTech Entrepreneurship, HealthTech Leadership, AgTech Business, Green Business Mgmt, Circular Economy Business, Social Commerce, Influencer Marketing, Affiliate Marketing, Search Engine Optimization, Growth Hacking, Business Law, Commercial Litigation, Mergers & Acquisitions, Corporate Governance, Sustainability Reporting, ESG Investing, Fintech Law, Algorithmic Trading Mgmt, Hedge Fund Mgmt, Sports Management, Luxury Brand Mgmt, Wine Business Mgmt, Casino Mgmt, Cruise Line Mgmt, Theme Park Mgmt, Museum Management, Art Market Mgmt, Political Consulting, Diplomacy, Intelligence Studies, Strategic Forecasting, Competitive Intelligence, Negotiation Science, Mediation & Arbitration, Contract Mgmt, Procurement Strategy", 
            "career": "Manager, Entrepreneur, Lawyer, Sales, PR Head, Hotelier, Digital Strategist",
            "skills": ["Leadership", "Business Strategy", "Negotiation", "Marketing"],
            "tech": ["Blockchain in Business", "Growth Hacking AI", "CRM Automation", "FinTech"],
            "sources": ["Harvard Business Review", "Google Digital Garage", "Y Combinator (Startup School)", "HubSpot Academy"]
        },
        "C": {
            "title": "Conventional (The Organizer)", 
            "traits": "Detailed, Structured, Efficient", 
            "courses": "B.Com, CA, Actuarial Science, Statistics, Logistics, Library Science, Information Management, Digital Forensics, Operations Research, Banking, Tax Consultancy, Cost Accounting, Financial Auditing, Management Accounting, Corporate Secretarial, Bookkeeping, Payroll Management, Tax Planning, Internal Audit, Compliance Management, Risk Auditing, Database Management, Data Entry Science, Records Management, Knowledge Management, Document Control, Technical Writing, Business Correspondence, Office Administration, Executive Assistantship, Secretarial Practice, Legal Stenography, Court Reporting, Medical Coding, Medical Transcription, Billing & Coding, Insurance Claims Processing, Underwriting, Credit Analysis, Mortgage Processing, Loan Documentation, Trade Finance Operations, Treasury Operations, Back Office Mgmt, Inventory Management, Warehouse Mgmt, Procurement Science, Strategic Sourcing, Supply Planning, Demand Planning, ERP Implementation (SAP/Oracle), Salesforce Admin, Cloud Data Management, Cybersecurity Compliance, IT Audit, Quality Assurance, Quality Control, Six Sigma, Lean Management, ISO Certification Mgmt, Standardization Science, Regulatory Affairs, Patent Filing, Trademark Admin, Library Science, Archival Studies, Museum Documentation, Statistical Analysis, Econometrics, Quantitative Finance, Fixed Income Analysis, Portfolio Admin, Fund Accounting, Estate Planning, Trust Management, Pension Fund Admin, AML Compliance, KYC Specialist, Fraud Investigation, Forensic Accounting, Customs Broking, Supply Chain Security, Logistical Analytics, Distribution Management, Fleet Management, Traffic Management, Urban Planning Admin, Public Registry Mgmt, Census Data Science, Voter Records Mgmt, Health Information Mgmt, Clinical Data Mgmt, Pharmaceutical Compliance, Lab Quality Mgmt, Environmental Compliance, Safety Auditing, Occupational Health Records, Financial Reporting, XBRL Tagging, IFRS Specialist, GAAP Auditor", 
            "career": "Accountant, Banker, Data Analyst, Admin, Actuary, Auditor, Logistics Head",
            "skills": ["Financial Planning", "Database Management", "Auditing", "Process Optimization"],
            "tech": ["Robotic Process Automation (RPA)", "Cloud Accounting", "Blockchain Ledger", "Cybersecurity"],
            "sources": ["Microsoft Learn", "IBM Data Science Professional", "QuickBooks Training", "W3Schools"]
        }
    },
    "colleges": [
        {"name": "NIT Calicut", "loc": "Calicut, Kerala", "streams": ["Engineering", "Science"], "courses": ["B.Tech CSE", "B.Tech Mech", "M.Sc Physics"], "cutoff": "JEE Main", "type": "National", "url": "https://www.nitc.ac.in/"},
        {"name": "CET Trivandrum", "loc": "Trivandrum, Kerala", "streams": ["Engineering", "Architecture"], "courses": ["B.Tech CSE", "B.Arch", "B.Tech EEE"], "cutoff": "KEAM Rank < 1000", "type": "State Govt", "url": "https://www.cet.ac.in/"},
        {"name": "TKM College", "loc": "Kollam, Kerala", "streams": ["Engineering", "Architecture"], "courses": ["B.Tech Civil", "B.Tech Mech", "B.Arch"], "cutoff": "KEAM", "type": "Aided", "url": "https://tkmce.ac.in/"},
        {"name": "Model Eng College", "loc": "Kochi, Kerala", "streams": ["Engineering"], "courses": ["B.Tech CSE", "B.Tech ECE", "B.Tech BME"], "cutoff": "KEAM Top Rank", "type": "Govt Controlled", "url": "https://www.mec.ac.in/"},
        {"name": "GEC Thrissur", "loc": "Thrissur, Kerala", "streams": ["Engineering", "Architecture"], "courses": ["B.Tech CSE", "B.Tech Production", "B.Arch"], "cutoff": "KEAM Rank < 2000", "type": "State Govt", "url": "https://gectcr.ac.in/"},
        {"name": "CUSAT", "loc": "Kochi, Kerala", "streams": ["Engineering", "Science", "Law", "Marine"], "courses": ["B.Tech Marine", "B.Tech Safety", "Integrated M.Sc"], "cutoff": "CUSAT CAT", "type": "State University", "url": "https://cusat.ac.in/"},
        {"name": "SCMS School of Eng", "loc": "Kochi, Kerala", "streams": ["Engineering"], "courses": ["B.Tech CSE", "B.Tech Auto"], "cutoff": "KEAM", "type": "Self Financing", "url": "https://scmsgroup.org/sset/"},
        {"name": "SCT College", "loc": "Trivandrum, Kerala", "streams": ["Engineering"], "courses": ["B.Tech Auto", "B.Tech Biotech"], "cutoff": "KEAM", "type": "State Govt", "url": "https://sctce.ac.in/"},
        {"name": "College of Engineering, Thalassery", "loc": "Thalassery, Kerala", "streams": ["Engineering"], "courses": ["B.Tech CSE", "B.Tech ECE"], "cutoff": "KEAM", "type": "Govt Controlled", "url": "http://www.cethalassery.ac.in/"},
        {"name": "University of Kerala", "loc": "Trivandrum, Kerala", "streams": ["Arts", "Science"], "courses": ["BA English", "M.Sc Physics", "Ph.D"], "cutoff": "Merit Based", "type": "University", "url": "https://www.keralauniversity.ac.in/"},
        {"name": "Sacred Heart College", "loc": "Kochi, Kerala", "streams": ["Arts", "Science", "Commerce"], "courses": ["BA Animation", "B.Com", "B.Sc Botany"], "cutoff": "Metit/Interview", "type": "Autonomous", "url": "https://shcollege.ac.in/"},
        {"name": "St. Teresa's College", "loc": "Kochi, Kerala", "streams": ["Arts", "Science"], "courses": ["BA French", "B.Sc Fashion", "B.Com"], "cutoff": "Merit", "type": "Autonomous", "url": "https://teresas.ac.in/"},
        {"name": "Maharaja's College", "loc": "Ernakulam, Kerala", "streams": ["Arts", "Science"], "courses": ["BA Music", "BA Pol Science", "B.Sc Chem"], "cutoff": "High Merit", "type": "Govt Autonomous", "url": "https://maharajas.ac.in/"},
        {"name": "Rajagiri College", "loc": "Kalamassery, Kerala", "streams": ["Commerce", "Arts"], "courses": ["BBA", "BSW", "MBA", "MCA"], "cutoff": "Entrance/Merit", "type": "Autonomous", "url": "https://rajagiri.edu/"},
        {"name": "NUALS", "loc": "Kochi, Kerala", "streams": ["Law", "Arts"], "courses": ["BA LLB (Hons)", "LLM"], "cutoff": "CLAT", "type": "National Law Univ", "url": "https://nuals.ac.in/"},
        {"name": "Govt. Medical College", "loc": "Kozhikode, Kerala", "streams": ["Science", "Medicine"], "courses": ["MBBS", "BDS", "B.Sc Nursing"], "cutoff": "NEET Top Rank", "type": "Govt", "url": "https://www.govtmedicalcollegekozhikode.ac.in/"},
        {"name": "Amrita School of Medicine", "loc": "Kochi, Kerala", "streams": ["Science", "Medicine"], "courses": ["MBBS", "B.Pharm"], "cutoff": "NEET", "type": "Private Deemed", "url": "https://www.amrita.edu/school/medicine/"},
        {"name": "IIT Madras", "loc": "Chennai, Tamil Nadu", "streams": ["Engineering", "Science"], "courses": ["B.Tech CSE", "B.Sc Data Science"], "cutoff": "JEE Advanced", "type": "National #1", "url": "https://www.iitm.ac.in/"},
        {"name": "IIT Delhi", "loc": "New Delhi", "streams": ["Engineering"], "courses": ["B.Tech CSE", "B.Tech MnC"], "cutoff": "JEE Advanced", "type": "National Elite", "url": "https://home.iitd.ac.in/"},
        {"name": "IIT Bombay", "loc": "Mumbai, Maharashtra", "streams": ["Engineering"], "courses": ["B.Tech CSE", "B.Des"], "cutoff": "JEE Advanced", "type": "National Elite", "url": "https://www.iitb.ac.in/"},
        {"name": "IIT Kanpur", "loc": "Kanpur, UP", "streams": ["Engineering"], "courses": ["B.Tech CSE", "B.Sc Maths"], "cutoff": "JEE Advanced", "type": "National Elite", "url": "https://www.iitk.ac.in/"},
        {"name": "IIT Kharagpur", "loc": "Kharagpur, WB", "streams": ["Engineering"], "courses": ["B.Tech", "B.Arch", "Law"], "cutoff": "JEE Advanced", "type": "National Elite", "url": "https://www.iitkgp.ac.in/"},
        {"name": "IIT Roorkee", "loc": "Roorkee, Uttarakhand", "streams": ["Engineering"], "courses": ["B.Tech", "B.Arch"], "cutoff": "JEE Advanced", "type": "National Elite", "url": "https://www.iitr.ac.in/"},
        {"name": "IIT Hyderabad", "loc": "Hyderabad, Telangana", "streams": ["Engineering"], "courses": ["B.Tech AI", "B.Des"], "cutoff": "JEE Advanced", "type": "National Elite", "url": "https://iith.ac.in/"},
        {"name": "SRCC", "loc": "New Delhi", "streams": ["Commerce"], "courses": ["B.Com Hons", "BA Economics"], "cutoff": "CUET Top 0.5%", "type": "Central Govt", "url": "https://www.srcc.edu/"},
        {"name": "LSR for Women", "loc": "New Delhi", "streams": ["Arts", "Commerce"], "courses": ["BA Psychology", "BA English", "B.Com"], "cutoff": "CUET", "type": "Premier Arts", "url": "https://lsr.edu.in/"},
        {"name": "St. Stephen's College", "loc": "New Delhi", "streams": ["Arts", "Science"], "courses": ["BA History", "B.Sc Physics"], "cutoff": "CUET + Interview", "type": "Premier Arts", "url": "https://www.ststephens.edu/"},
        {"name": "Loyola College", "loc": "Chennai, Tamil Nadu", "streams": ["Arts", "Science", "Commerce"], "courses": ["B.Sc Visual Comm", "B.Com", "BA Economics"], "cutoff": "Merit", "type": "Premier", "url": "https://www.loyolacollege.edu/"},
        {"name": "Christ University", "loc": "Bangalore, Karnataka", "streams": ["Commerce", "Arts", "Science", "Law"], "courses": ["BBA", "B.Com", "BA Psychology", "LLB"], "cutoff": "Combined Entrance", "type": "Global Standard", "url": "https://christuniversity.in/"},
        {"name": "Symbiosis Institue", "loc": "Pune, Maharashtra", "streams": ["Design", "Law", "Management"], "courses": ["B.Des", "BBA LLB", "BBA"], "cutoff": "SET/SEED", "type": "Elite Private", "url": "https://www.siu.edu.in/"},
        {"name": "TISS", "loc": "Mumbai, Maharashtra", "streams": ["Social", "Arts"], "courses": ["BSW", "BA Social Science"], "cutoff": "TISS-BAT", "type": "National Specialized", "url": "https://www.tiss.edu/"},
        {"name": "NID Ahmedabad", "loc": "Ahmedabad, Gujarat", "streams": ["Arts", "Design"], "courses": ["B.Des Product", "B.Des Graphic"], "cutoff": "NID DAT", "type": "Central Govt", "url": "https://www.nid.edu/"},
        {"name": "NIFT Delhi", "loc": "New Delhi", "streams": ["Design"], "courses": ["B.Des Fashion", "B.FTech"], "cutoff": "NIFT Entrance", "type": "Central Govt", "url": "https://www.nift.ac.in/"},
        {"name": "AIIMS", "loc": "New Delhi", "streams": ["Medicine", "Science"], "courses": ["MBBS", "B.Sc Nursing"], "cutoff": "AIIMS Entrance", "type": "National #1", "url": "https://www.aiims.edu/"},
        {"name": "AFMC", "loc": "Pune, Maharashtra", "streams": ["Medicine"], "courses": ["MBBS", "B.Sc Nursing"], "cutoff": "NEET + Interview", "type": "Defense Govt", "url": "https://afmc.nic.in/"},
        {"name": "CMC Vellore", "loc": "Vellore, Tamil Nadu", "streams": ["Medicine", "Science"], "courses": ["MBBS", "B.Sc Nursing", "BPT"], "cutoff": "NEET + Internal", "type": "Private Premier", "url": "https://www.cmcvellore.ac.in/"},
        {"name": "LPU", "loc": "Phagwara, Punjab", "streams": ["Engineering", "Arts", "Science", "Commerce", "Design"], "courses": ["B.Tech", "B.Des", "MBA", "BA"], "cutoff": "LPUNEST", "type": "Global Campus", "url": "https://www.lpu.in/"},
        {"name": "IARI New Delhi", "loc": "Delhi", "streams": ["Science"], "courses": ["B.Sc Agriculture", "M.Sc Agriculture"], "cutoff": "ICAR AIEEA", "type": "National Elite", "url": "https://www.iari.res.in/"},
        {"name": "Gujarat Forensic Sciences Univ", "loc": "Gandhinagar", "streams": ["Science"], "courses": ["B.Sc Forensic Science", "Cybersecurity"], "cutoff": "Entrance Test", "type": "National Specialized", "url": "https://www.nfsu.ac.in/"},
        {"name": "National Rail & Transp Inst", "loc": "Vadodara", "streams": ["Engineering", "Management"], "courses": ["B.Tech Robotics", "BBA Logistics"], "cutoff": "CUET", "type": "National Specialized", "url": "https://nrti.edu.in/"},
        {"name": "IGRUA", "loc": "Amethi, UP", "streams": ["Science"], "courses": ["Commercial Pilot Training"], "cutoff": "Entrance/Medical", "type": "National Premier", "url": "https://igrua.gov.in/"},
        {"name": "IHM Pusa", "loc": "New Delhi", "streams": ["Management"], "courses": ["B.Sc Hotel Management", "Culinary Arts"], "cutoff": "NCHMCT JEE", "type": "National #1", "url": "https://ihmpusa.net/"},
        {"name": "TISS Mumbai", "loc": "Mumbai", "streams": ["Social", "Arts"], "courses": ["BSW", "BA Social Science"], "cutoff": "CUET", "type": "National Elite", "url": "https://www.tiss.edu/"},
        {"name": "MICA Ahmedabad", "loc": "Ahmedabad", "streams": ["Management", "Arts"], "courses": ["Digital Marketing", "Mass Comm"], "cutoff": "MICAT", "type": "National Specialized", "url": "https://www.mica.ac.in/"},
        {"name": "NID Bangalore", "loc": "Bangalore", "streams": ["Design"], "courses": ["B.Des Interaction", "B.Des Tech"], "cutoff": "NID DAT", "type": "Central Govt", "url": "https://www.nid.edu/"},
        {"name": "PAU Ludhiana", "loc": "Ludhiana, Punjab", "streams": ["Science"], "courses": ["B.Sc Forestry", "Agriculture"], "cutoff": "PAU Entrance", "type": "State Elite", "url": "https://www.pau.edu/"},
        {"name": "BITS Pilani", "loc": "Pilani, Rajasthan", "streams": ["Engineering", "Science"], "courses": ["B.Tech CS", "B.Pharm", "M.Sc Eco"], "cutoff": "BITSAT", "type": "Private Elite", "url": "https://www.bits-pilani.ac.in/"},
        {"name": "IIIT Hyderabad", "loc": "Hyderabad", "streams": ["Engineering"], "courses": ["B.Tech CSE", "B.Tech AI"], "cutoff": "JEE Main/UGEE", "type": "National Elite", "url": "https://www.iiit.ac.in/"},
        {"name": "IIM Indore (Integrated)", "loc": "Indore", "streams": ["Management"], "courses": ["IPM (BBA+MBA)"], "cutoff": "IPMAT", "type": "National Elite", "url": "https://www.iimidr.ac.in/"},
        {"name": "National Insurance Academy", "loc": "Pune", "streams": ["Commerce"], "courses": ["Actuarial Science", "Insurance Mgmt"], "cutoff": "Entrance", "type": "National Specialized", "url": "https://niapune.org.in/"},
        {"name": "FTII Pune", "loc": "Pune", "streams": ["Arts"], "courses": ["Film Studies", "Sound Engineering", "Animation"], "cutoff": "JET Entrance", "type": "National Elite", "url": "https://www.ftii.ac.in/"},
        {"name": "MIT", "loc": "Cambridge, USA", "streams": ["Engineering", "Science"], "courses": ["BS CS", "BS Physics", "Engineering"], "cutoff": "SAT/ACT + Portfolio", "type": "Global #1", "url": "https://www.mit.edu/"},
        {"name": "Imperial College", "loc": "London, UK", "streams": ["Engineering", "Science", "Medicine"], "courses": ["B.Eng", "MBBS", "B.Sc"], "cutoff": "A-Levels/IB", "type": "Global Top 10", "url": "https://www.imperial.ac.uk/"},
        {"name": "Stanford University", "loc": "California, USA", "streams": ["Engineering", "Arts", "Science"], "courses": ["BS CS", "BA Economics"], "cutoff": "SAT/ACT", "type": "Global Top 10", "url": "https://www.stanford.edu/"},
        {"name": "University of Oxford", "loc": "Oxford, UK", "streams": ["Arts", "Science", "Medicine"], "courses": ["PPE", "Medicine", "Law"], "cutoff": "A-Levels/IB", "type": "Global Top 10", "url": "https://www.ox.ac.uk/"},
        {"name": "Harvard University", "loc": "Cambridge, USA", "streams": ["Arts", "Science", "Law"], "courses": ["BA Liberal Arts", "Law"], "cutoff": "SAT/ACT", "type": "Global Top 10", "url": "https://www.harvard.edu/"},
        {"name": "NUS", "loc": "Singapore", "streams": ["Engineering", "Science"], "courses": ["B.Eng", "B.Comp"], "cutoff": "High Merit", "type": "Asia Top", "url": "https://www.nus.edu.sg/"},
        {"name": "ETH Zurich", "loc": "Zurich, Switzerland", "streams": ["Engineering", "Science"], "courses": ["BS Physics", "BS Mech Eng"], "cutoff": "Entrance Exam", "type": "Europe Top", "url": "https://ethz.ch/"}
    ]
}

# Integrate extracted career data
import json
import os

try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(BASE_DIR, '..', 'occupations_data.json')
    with open(json_path, 'r') as f:
        CAREERS_DATA = json.load(f)
    DATA["careers"] = CAREERS_DATA
except Exception as e:
    print(f"Error loading career data: {e}")
    DATA["careers"] = {}
