import google.generativeai as palm
from dotenv import load_dotenv
from src.DB import *
import os

load_dotenv()
api_key = os.environ.get("PALM_API_KEY")
palm.configure(api_key=api_key)

Article1 = """Article 1. Nomenclature of the state
This Constitution establishes a Federal and Democratic State structure. Accordingly, the
Ethiopian state shall be known as The Federal Democratic Republic of Ethiopia."""

Article2 = """Article 2. Ethiopian Territorial Jurisdiction
The territorial jurisdiction of Ethiopia shall comprise the territory of the members of the
Federation and its boundaries shall be as determined by international agreements."""

Article3 = """Article 3. The Ethiopian Flag
1. The Ethiopian flag shall consist of green at the top, yellow in the middle and red at the bottom,
and shall have a national emblem at the center. The three colours shall be set horizontally in
equal dimension.
2. The national emblem on the flag shall reflect the hope of the Nations, Nationalities, Peoples as
well as religious communities of Ethiopia to live together in equality and unity.
3. Members of the Federation may have their respective flags and emblems and shall determine
the details thereof through their respective legislatures."""

Article4 = """Article 4. National Anthem of Ethiopia
The national anthem of Ethiopia, to be determined by law.
shall reflect the ideals of the Constitution, the commitment of the Peoples of Ethiopia to live
together in a democratic order, and of their common destiny."""

Article5 = """Article 5. Languages
1. All Ethiopian languages shall enjoy equal state recognition
2. Amharic shall be the working language of the Federal Government.
3. Members of the Federation may by law determine their respective working languages."""

Article6 = """Article 6. Nationality
1. Any person of either sex shall be an Ethiopian national where both or either parent is
Ethiopian.
2. Foreign nationals may acquire Ethiopian nationality.
3. Particulars relating to nationality shall be determined by law."""

Article7 = """Article 7. Gender Reference
Provisions of this Constitution set out in the masculine gender shall also apply to the feminine
gender"""

Article8 = """Article 8. Sovereignty of the People
1. All sovereign power resides in the Nations, Nationalities and Peoples of Ethiopia.
2. This Constitution is an expression of their sovereignty.
3. Their sovereignty shall be expressed through their representatives elected in accordance with
this Constitution and through their direct, democratic participation."""

Article9 = """Article 9. Supremacy of the Constitution
1. The Constitution is the supreme law of the land. Any law, customary practice or a decision of
an organ of state or a public official which contravenes this Constitution shall be of no effect.
2. All citizens, organs of state, political organizations, other associations as well as their officials
have the duty to ensure observance of the Constitution and to obey it.
3. It is prohibited to assume state power in any manner other than that provided under the
Constitution.
4. All international agreements ratified by Ethiopia are an integral part of the law of the land."""

Article10 = """Article 10. Human and Democratic Rights
1. Human rights and freedoms, emanating from the nature of mankind, are inviolable and
inalienable.
2. Human and democratic rights of citizens and peoples shall be respected."""

Article11 = """Article 11. Separation of State and Religion
1. State and religion are separate.
2. There shall be no state religion.
3. The state shall not interfere in religious masters and religion shall not interfere in state affairs."""

Article12 = """Article 12. Conduct and Accountability of Government
1. The conduct of affairs of government shall be transparent.
2. Any public official or an elected representative is accountable for any failure in official duties.
3. In case of loss of confidence, the people may recall an elected representative. The particulars
of recall shall be determined by law."""

Article13 = """Article 13. Scope of Application and Interpretation
1. All Federal and State legislative, executive and judicial organs at all levels shall have the
responsibility and duty to respect and enforce the provisions of this Chapter.
2. The fundamental rights and freedoms specified in this Chapter shall be interpreted in a manner
conforming to the principles of the Universal Declaration of Human Rights, International
Covenants on Human Rights and International instruments adopted by Ethiopia."""

Article14 = """Article 14. Rights to life, the Security of Person and Liberty
Every person has the inviolable and inalienable right to life, the security of person and liberty."""

Article15 = """Article 15. Right to Life
Every person has the right to life. No person may be deprived of his life except as a punishment
for a serious criminal offence determined by law."""

Article16 = """Article 16. The Right of the Security of Person
Every one has the right to protection against bodily harm."""

Article17 = """Article 17. Right to Liberty
1. No one shall be deprived of his or her liberty except on such grounds and in accordance with
such procedure as are established by law.
2. No person may be subjected to arbitrary arrest, and no person may be detained without a
charge or conviction against him."""

Article18 = """Article 18. Prohibition against Inhuman Treatment
1. Everyone has the right to protection against cruel, inhuman or degrading treatment or
punishment.
2. No one shall be held in slavery or servitude. Trafficking in human beings for whatever
purpose is prohibited:
3. No one shall be required to perform forced or compulsory labour.
4. For the purpose of sub-Article 3 of this Article the phrase "forced or compulsory labour" shall
not include:
(a) Any work or service normally required of a person who is under detention in consequence of
a lawful order, or of a person during conditional release from such detention;
(b) In the case of conscientious objectors, any service exacted in lieu of compulsory military
service;
(c) Any service exacted in cases of emergency or calamity threatening the life or well-being of
the community;
(d) Any economic and social development activity voluntarily performed by a community within
its locality."""

Article19 = """Article 19. The Right of Persons Arrested
1. Persons arrested have the right to be informed promptly, in a language they understand, of the
reasons for their arrest and of any charge against them.
2. Persons arrested have the right to remain silent. Upon arrest, they have the right to be
informed promptly, in a language they understand, that any statement they make may be used as
evidence against them in court.
3. Persons arrested have the right to be brought before a court within 48 hours of their arrest.
Such time shall not include the time reasonably required for the journey from the place of arrest
to the court. On appearing before a court, they have the right to be given prompt and specific
explanation of the reasons for their arrest due to the alleged crime committed.
4. All persons have an inalienable right to petition the court to order their physical release where
the arresting police officer or the law enforcer fails to bring" them before a court within the
prescribed time and to provide reasons for their arrest. Where the interest of justice requires, the
court may order the arrested person to remain in custody or, when requested, remand him for a
time strictly required to carry out the necessary investigation. In determining the additional time
necessary for investigations, the court shall ensure that the responsible law enforcement
authorities carry out the investigation respecting the arrested person's right to a speedy trial.
5. Persons arrested shall not be compelled to make confessions or admissions which could be
used in evidence or against them. Any evidence obtained under coercion shall not be admissible.
6. Persons arrested have the right to be released on bail. In exceptional circumstances prescribed
by law, the court may deny bail or demand adequate guarantee for the conditional release of the
arrested person."""

Article20 = """Article 20. Rights of Persons Accused
1. Accused persons have the right to a public trial by an ordinary court of law within a
reasonable time after having been charged. The court may hear cases in a closed session only
with a view to protecting the right to privacy of the parties concerned, public morals and
national security.
2. Accused persons have the right to be informed with sufficient particulars of the charge brought
against them and to be given the charge in writing
3. During proceedings accused persons have the right to be presumed innocent until proved
guilty according to law and not to be compelled to testify against themselves.
4. Accused persons have the right to full access to any evidence presented against them, to
examine witnesses testifying against them, to adduce or to have evidence produced in their own
defence, and to obtain the attendance of and: examination of witnesses on their behalf before the
court.
5. Accused persons have the right to be represented by legal counsel of their choice, and, if they
do not have sufficient means to pay for it and miscarriage of justice would result, to be provided
with legal representation at state expense
6. All persons have the right of appeal to the competent court against an order or a judgement of
the court which first heard the case.
7. They have the right to request for the assistance of an interpreter at state expense where the
court proceedings are conducted in a language they do not understand."""

Article21 = """Article 21. The Rights of Persons Held in Custody and Convicted Prisoners
l. All persons held in custody and persons imprisoned upon conviction and sentencing have the
right to treatments respecting their human dignity.
2. All persons shall have the opportunity to communicate with, and to be visited by, their spouses
or partners, close relatives, friends, religious councilors, medical doctors and their legal counsel."""

Article22 = """Article 22. Non-retroactively of Criminal Law
1. No one shall be held guilty of any criminal offence on account of any act or omission which
did not constitute a criminal offence at the time when it was committed. Nor shall a heavier
penalty be imposed on any person than the one that was applicable at the time when the criminal
offence was committed.
2. Notwithstanding the provisions of sub-Article 1 of this Article, a law promulgated subsequent
to the commission of the offence shall apply if it is advantageous to the accused or convicted
person."""

Article23 = """Article 23. Prohibition of Double Jeopardy
No person shall be liable to be tried or punished again for an offence for which he has already
been finally convicted or acquitted in accordance with the criminal law and procedure."""

Article24 = """Article 24. Right to Honour and Reputation
1. Everyone has the right to respect for his human dignity, reputation and honour.
2. Everyone has the right to the free development of his personality in a manner compatible with
the rights of other citizens.
3. Everyone has the right to recognition everywhere as a person."""

Article25 = """Article 25. Right to Equality
All persons are equal before the law and are entitled without any discrimination to the equal
protection of the law. In this respect, the law shall guarantee to all persons equal and effective
protection without discrimination on grounds of race, nation, nationality, or other social origin,
colour, sex, language, religion, political or other opinion, property, birth or other status."""

Article26 = """Article 26. Right to Privacy
1. Everyone has the right to privacy. This right shall include the right not to be subjected to
searches of his home, person or property, or the seizure of any property under his personal
possession.
2. Everyone has the right to the inviolability of his notes and correspondance including postal
letters, and communications made by means of telephone , telecommunications and electronic
devices.
3. Public officials shall respect and protect these rights. No restrictions may be placed on the
enjoyment of such rights except in compelling circumstances and in accordance with specific
laws whose purposes shall be the safeguarding of national security or public peace, the
prevention of crimes or the protection of health, public morality or the rights and freedoms of
others, and to ensure the independence of the state from religion.
Any citizen who violates any legal limitations on the exercice of these rights may be held
liable under the law."""

Article27 = """Article 27. Freedom of Religion, Belief and Opinion
1. Everyone has the right to freedom of thought, conscience and religion. This right shall include
the freedom to hold or to adopt a religion or belief of his choice, and the freedom, either
individually or in community with others, and in public or private, to manifest his religion or
belief in worship, observance, practice and teaching.
2. Without prejudice to the provisions of sub-Article 2 of Article 90, believers may establish
institutions of religious education and administration in order to propagate and organize their
religion.
3. No one shall be subject to coercion or other means which would restrict or prevent his
freedom to hold a belief of his choice.
4. Parents and legal guardians have the right to bring up their children ensuring their religious
and moral education in conformity with their own convictions.
5. Freedom to express or manifest one's religion or belief may be subject only to such limitations
as are prescribed by law and are necessary to protect public safety, peace, health; education,
public morality or the fundamental rights and freedoms of others, and to ensure the independence
of the state from religion.
Any citizen who violates any legal limitations on the exercice of these rights may be held
liable under the law."""

Article28 = """Article 28. Crimes against Humanity
1. Criminal liability of persons who commit crimes against humanity, so defined by international
agreements ratified by Ethiopia and by other laws of Ethiopia, such as genocide, summary
executions, forcible disappearances or torture shall not be barred by statute of limitation. Such
offences may not be commuted by amnesty or pardon of the legislature or any other state organ.
2. In the case of persons convicted of any crime stated in sub-Article I of this Article and
sentenced with the death penalty, the Head of State may, without prejudice to the provisions
hereinabove, commute the punishment to life imprisonment."""

Article29 = """Article 29. Right of Thought, Opinion and Expression
1. Everyone has the right to hold opinions without interference.
2. Everyone has the right to freedom of expression without any interference. This right shall
include freedom to seek, receive and impart information and ideas of all kinds, regardless of
frontiers, either orally, in writing or in print, in the form of art, or through any media of his
choice.
3. Freedom of the press and other mass media and freedom of artistic creativity is guaranteed.
Freedom of the press shall specifically include the following elements:
(a) Prohibition of any form of censorship.
(b) Access to information of public interest.
4. In the interest of the free flow of information, ideas and opinions which are essential to the
functioning of a democratic order, the press shall, as an institution, enjoy legal protection to
ensure its operational independence and its capacity to entertain diverse opinions.
5. Any media financed by or under the control of the State, shall be operated in a manner
ensuring its capacity to entertain diversity in the expression of opinion.
6. These rights can be limited only through laws which are guided by the principle that freedom
of expression and information cannot be limited on account of the content or effect of the point
of view expressed. Legal limitation can be laid down in order to protect the well-being of the
youth, and the honour and reputation of individuals. An propaganda for war as well as the public
expression of opinion intended to injure human dignity shall be prohibited by law.
7. Any citizen who violates any legal limitations on the exercice of these rights may be held
liable under the law."""

Article30 = """Article 30. The Right of Assembly, Demonstration and petition
1. Everyone has the right to assemble and to demonstrate together with others peaceably and
unarmed, and to petition. Appropriate regulations may be made in the interest of public
convenience relating to the location of open-air meetings and the route of movement of
demonstrators or, for the protection of democratic rights, public morality and peace during such a
meeting or demonstration.
2. This right does not exempt from liability under law enacted to protect the well-being of the
youth or the honour and reputation of individuals, and laws prohibiting any propaganda for war
and any public expression of opinions intended to injure human dignity."""

Article31 = """Article 31. Freedom of Association
Every person has the right to freedom of association for any cause or purpose. Organizations
formed, in violation appropriate laws, or to illegally subvert the constitutional order, or which
promote such activities are prohibited."""

Article32 = """Article 32. Freedom of Movement
1. Any Ethiopian or foreign national lawfully in Ethiopia has, within the national territory, the
right to liberty of movement and freedom to choose his residence, as well as the freedom to leave
the country at any time he wishes to.
2. Any Ethiopian national has the right to return to country."""

Article33 = """Article 33. Rights of nationality
1. No Ethiopian national shall be deprived of his or her Ethiopian nationality against his or her
will. Marriage of an Ethiopian national of either sex to a foreign national shall not annul his or
her Ethiopian nationality.
2. Every Ethiopian national has the right to the enjoyment of all rights, protection and benefits
derived from Ethiopian nationality as prescribed by law.
3. Any national has the right to change his Ethiopian nationality.
4. Ethiopian nationality may be conferred upon foreigners in accordance with law enacted and
procedures established consistent with international agreements ratified by Ethiopia."""

articles = [
    Article1,
    Article2,
    Article3,
    Article4,
    Article5,
    Article6,
    Article7,
    Article8,
    Article9,
    Article10,
    Article11,
    Article12,
    Article13,
    Article14,
    Article15,
    Article16,
    Article17,
    Article18,
    Article19,
    Article20,
    Article21,
    Article22,
    Article23,
    Article24,
    Article25,
    Article26,
    Article27,
    Article28,
    Article29,
    Article30,
    Article31,
    Article32,
    Article33,
]

# Selecting the first and only text generation model available in palm
text_model = [
    m for m in palm.list_models() if "generateText" in m.supported_generation_methods
][0]


def init():
    db = create_chroma_db(articles, "laws")
    return db, text_model


def make_prompt(query, context):
    escaped = context.replace("'", "").replace('"', "").replace("\n", " ")
    prompt = (
        """ You are Enderase/እንደራሴ, a friendly and knowledgeable legal bot with expertise in Ethiopian law. Your extensive training is based on a wealth of Ethiopian legal documents, enabling you to provide comprehensive answers to questions using onlythe text data provided below not any legal information you have been trained on before. When responding, please use complete sentences, break down complex legal concepts into understandable terms, and maintain a professional yet approachable tone. If the provided text doesn't contain sufficient information to address a user's query, kindly respond with only 'There is not enough context. I am currenlty on Experimental stage and will incorporate more context soon.'. Remember to cite the relevant legal articles and suggest seeking advice from legal professionals if uncertainty arises. You may disregard irrelevant passages when formulating your responses. You should format your output in a userfreindly and readable structure.
  QUESTION: '{query}'
  PASSAGE: '{context}'

    ANSWER:
  """
    ).format(query=query, context=escaped)

    return prompt


def generate(model, query, db, temperature=0.1):
    prompt = make_prompt(query, context="")
    answer = palm.generate_text(
        prompt=prompt,
        model=model,
        candidate_count=3,
        temperature=temperature,
        max_output_tokens=1000,
    )
    if len(answer.candidates) > 0:
        return answer.candidates[0]["output"]
    else:
        return "Server encountered some error. Retry in just a moment"
