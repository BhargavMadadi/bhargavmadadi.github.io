from backend import top3

print(top3('cold'))
cold_list = ['''Ginger is known for its anti-inflammatory and anti-microbial properties, and honey has been shown to have natural antibacterial properties. This tea can help soothe a sore throat, alleviate congestion and cough, and provide some relief from cold symptoms.''', 
'''Garlic is known for its antibacterial and antiviral properties, and may help boost the immune system. Lemon juice contains vitamin C, which is also known for relieving cold symptoms.''', 
'''Tulsi, also known as holy basil, is a popular herb in Ayurvedic medicine and is believed to have antiviral, antibacterial, and anti-inflammatory properties. Drinking tulsi tea may help alleviate cold symptoms such as cough, congestion, and fever.''']


print(top3('fever'))
fever_list = ['''Some people may prefer their okayu to be more soupy or thicker, so feel free to adjust the water ratio to your liking. You can also experiment with different toppings, such as soy sauce, sesame seeds, or cooked vegetables. Okayu can be a gentle and nourishing food for those with upset stomachs, and the ginger is thought to have anti-inflammatory and digestive benefits.''',
'''Bananas are a good source of vitamin C, vitamin B6, and potassium, which can help support the immune system and regulate body temperature. Oats are also a good source of fiber, which can help regulate digestion and promote healthy bowel movements. This porridge is a comforting and nourishing option that may help alleviate fever symptoms. However, it's important to note that if the fever persists or worsens, it's always a good idea to consult with a healthcare professional.''', 
'''Khichdi is a traditional Indian comfort food that's easy to make and easy to digest. It's a one-pot meal that's perfect for when you're feeling under the weather, as it's gentle on the stomach and packed with nutrients from the rice and dal. You can adjust the spice level to your liking by adding more or less green chilies and red chili powder. You can also add some chopped vegetables, such as carrots, peas, or cauliflower, to the khichdi for extra nutrition.''']



print(top3('sore throat'))
sore_throat_list = ['''Honey has natural antibacterial and anti-inflammatory properties, while lemon contains vitamin C which may help boost the immune system. Drinking honey and lemon tea may help alleviate sore throat symptoms and also provide some relief for coughing and congestion.''',
'''Turmeric has anti-inflammatory and antioxidant properties, and is commonly used in Indian cuisine and traditional medicine. The warm milk can also help soothe a sore throat and provide some relief from discomfort. Honey can also help soothe a sore throat and add a touch of sweetness to the drink.''',
'''Salt has natural antibacterial properties that can help kill off bacteria and viruses in the throat. Salt water can help soothe the throat and provide temporary relief from pain and discomfort and it can also help loosen mucus and phlegm which can make it easier to cough up any congestion in the throat and respiratory tract.''']



print(top3('headache'))
headache_list = ['''Peppermint and chamomile are both soothing herbs that can help alleviate headaches and promote relaxation. Lemon juice provides a refreshing burst of flavor and can help boost the immune system. Honey or agave nectar provide natural sweetness without the use of refined sugar. Note that if you experience persistent or severe headaches, it's important to consult with a healthcare provider to determine the underlying cause and appropriate treatment.''', 
'''Lavender, chamomile, and peppermint are all well-known for their soothing properties and can help reduce tension and stress, which are common causes of headaches. Honey or agave nectar can be added for natural sweetness if desired. Note that while herbs can be helpful for managing headaches, it's important to consult with a healthcare provider if you experience persistent or severe headaches to rule out any underlying medical conditions.''', 
'''Ginger and turmeric are both anti-inflammatory and have been traditionally used to alleviate headaches. Vegetables and brown rice provide vitamins, minerals, and fiber that can support overall health and well-being. Note that if you experience persistent or severe headaches, it's important to consult with a healthcare provider to determine the underlying cause and appropriate treatment.''']

print(top3('stuffy nose'))
stuffy_nose_list = ['''Ginger and cinnamon are warming herbs that can help increase blood flow and promote nasal decongestion, while lemon contains vitamin C that can boost the immune system and help fight off colds and flu. Honey is a natural antibacterial and can help soothe sore throats and irritated sinuses.''',
'''Ginger and cinnamon are warming herbs that can help increase blood flow and promote nasal decongestion, while lemon contains vitamin C that can boost the immune system and help fight off colds and flu. Honey is a natural antibacterial and can help soothe sore throats and irritated sinuses.'''
'''Beetroot is high in nitrates, which can help increase blood flow and improve nasal congestion. Carrots are rich in beta-carotene, which can help support the immune system, while ginger has anti-inflammatory and pain-relieving properties. Apples contain quercetin, a flavonoid that can help reduce inflammation and allergic reactions.''']


print(top3('cough'))
cough_list = ['''The thyme, sage, and oregano leaves contain natural compounds that have antiviral, antibacterial, and anti-inflammatory properties. These herbs can help to soothe the throat, reduce inflammation, and boost the immune system. The honey acts as a natural cough suppressant and helps to soothe the throat.''', 
'''Cloves have natural antibacterial and anti-inflammatory properties that can help to soothe the respiratory tract and relieve cough. The warm milk can help to relax the muscles in the throat and provide a soothing effect, while the honey can add a touch of sweetness and also has antibacterial properties. This recipe is simple to make and can be a comforting and effective remedy for cough, especially when consumed before bed.''',
'''The apple cider vinegar in this recipe can help to thin mucus and make it easier to cough up, while the honey can help to soothe the throat and reduce coughing. Ginger has natural anti-inflammatory properties that can help to reduce inflammation in the throat and airways. This natural cough remedy is easy to make and can be a great alternative to over-the-counter cough medicines.''']


print(top3('diarrhea'))
diarrhea_list = ['''This recipe works well for diarrhea because white rice is easily digestible and can help absorb excess water in the digestive system. Bananas are also easy to digest and can help soothe the digestive system, while providing essential vitamins and minerals. The salt in this recipe can help replenish electrolytes that may have been lost during diarrhea.''',
'''This rice pudding recipe can be a gentle and soothing food for someone experiencing diarrhea. The rice is easy to digest and the milk and sugar provide some nourishment and energy. The cinnamon is also thought to have anti-inflammatory properties, which can be beneficial for easing digestive discomfort.''', 
'''It's important to note that if diarrhea persists for more than a few days, is accompanied by severe pain or fever, or if you have other medical conditions, it's important to seek medical attention. Additionally, some individuals may have allergies or sensitivities to certain spices or herbs, so be sure to consult with a healthcare provider before trying this recipe.''']


print(top3('nausea'))
nausea_list = ['''This simple meal is easy to digest and may help soothe the stomach. Bananas are rich in potassium, which can help regulate the balance of fluids in the body and alleviate nausea. Oatmeal is also easy on the stomach and can provide a good source of fiber and nutrients.''',
'''Peppermint is a natural antispasmodic that can help to relax the muscles of the digestive tract, relieving cramps and spasms that can cause nausea. It also has a soothing effect on the stomach and may help to reduce inflammation. If you do not have dried peppermint leaves, you can use fresh peppermint leaves or peppermint oil.''',
'''The ginger in this recipe has natural anti-inflammatory and digestive properties that can help to calm the stomach and reduce nausea. Mint leaves can also have a soothing effect on the digestive system. Honey and lemon can help to add a touch of sweetness and acidity, respectively, to balance the flavor. This natural remedy is easy to make and can be a great alternative to over-the-counter anti-nausea medications.''']


print(top3('constipation'))
constipation_list = ['''Senna leaves are a natural laxative that can help to stimulate bowel movements and relieve constipation. Dandelion leaves can help to stimulate the liver and gallbladder, which can improve digestion and help to eliminate waste from the body. Fennel seeds have antispasmodic properties that can help to relax the muscles in the digestive tract, which can relieve cramping and promote regularity. This herbal tea can be a gentle and effective way to help relieve constipation naturally.''',
'''Warm lemon water can help to stimulate bowel movements and relieve constipation. Lemon juice is a natural diuretic and can help to flush out toxins and waste from the body. It also contains citric acid, which can help to stimulate the digestive system and promote the production of digestive juices. Additionally, warm water helps to soften the stool and make it easier to pass.''', 
'''This high fiber veggie stir-fry is packed with fiber, which can help to promote regularity and prevent constipation. The vegetables provide both soluble and insoluble fiber, which can help to soften the stool and make it easier to pass. The quinoa or brown rice also provides additional fiber, as well as complex carbohydrates to keep you feeling full and satisfied. Additionally, the garlic and onion can help to stimulate the digestive system and promote healthy gut bacteria.''']


print(top3('stomachache'))
stomachache_list = ['''This soup is easy on the stomach and contains ginger, which has natural anti-inflammatory properties that can help soothe an upset stomach. The cooked rice is also easy to digest and can provide a bland base for the soup.''',
'''This recipe contains ingredients that are believed to help soothe stomach ache in Ayurveda. Ginger has anti-inflammatory properties and can help ease stomach discomfort, while cumin seeds, coriander seeds, and fennel seeds are known for their digestive benefits and can help reduce bloating and indigestion. Honey also has antibacterial and anti-inflammatory properties that may help soothe a sore stomach.''', 
'''Dried tangerine peel (chenpi) is commonly used in traditional Chinese medicine for digestive problems, including stomach ache. It is believed to regulate the qi (energy flow) in the stomach, improve digestion, and alleviate stomach pain. Ginger is also commonly used in Chinese medicine for its anti-inflammatory and analgesic properties, and is believed to help with stomach cramps and bloating. Drinking this mixture slowly can also help relax the stomach muscles and alleviate pain.''']


print(top3('earache'))
earache_list = ['''A warm compress can help to relieve pain and reduce inflammation in the ear. The warmth can also help to improve blood flow to the area, which can promote healing. Be sure to use warm, not hot water, to avoid burning the skin.''',
'''Onions contain a flavonoid called quercetin, which has anti-inflammatory properties. This can help with relieving ear pain or swelling.''',
'''Basil oil has natural anti-inflammatory and analgesic properties that can help to soothe the pain and inflammation associated with earaches. It also has antibacterial properties that can help to fight off any infection that may be causing the earache.''']


print(top3('toothache'))
toothache_list = ['''Clove and ginger have natural analgesic and anti-inflammatory properties that can help to alleviate toothache pain, while cayenne pepper can help to reduce inflammation and increase circulation to the affected area. Coconut oil and honey have natural antibacterial properties and can help to soothe the affected area.''',
'''Helps to freshen breath. Reduces gingivitis. Helps to keep teeth and gum strong. Quick, short-term relief from toothache.''',
'''You can use coconut oil to dilute the clove oil and apply it to the gums. If you do not have clove oil, you can put cloves directly in the corner of your mouth and suck on them slowly.''']

print(top3('trouble breathing'))
trouble_breathing_list = ['''Warm and hot drinks can help loosen up the airways and relieve congestion. According to one study, the common source of respiratory infections, the respiratory syncytial virus, may be successfully combated by ginger.''', 
'''An early study showed that caffeine can reduce tightness in the muscles in a person’s airway. It alters the breathing pattern by increasing tidal volume and lengthening the inspiratory phase of the respiratory cycle. Or in short, helps you breathe easier for a little while (generally up to 4 hours).''', 
'''This Ayurvedic juice recipe is a simple and effective natural remedy for relieving trouble breathing. Ginger juice and lemon juice have natural anti-inflammatory and antibacterial properties, while honey can help soothe irritation in the throat and airways. The combination of these ingredients can help to ease congestion and improve breathing. It is recommended to drink this juice once or twice a day until symptoms improve.''']


print(top3('skin irritation'))
skin_irritation_list = ['''This turmeric paste can be used topically to soothe skin irritation.''',
'''This oatmeal bath can help to soothe skin irritation and provide relief from itching, inflammation, and other symptoms.''',
'''Calendula is known for its anti-inflammatory and skin-soothing properties, so it can be helpful for a variety of skin irritations, such as rashes, insect bites, and minor cuts and scrapes.''']


print(top3('muscle pain'))
muscle_pain_list = ['''The cayenne and ginger work to improve circulation and reduce inflammation, while the peppermint oil provides a cooling sensation and further helps to soothe sore muscles.''',
'''This might be just what you need to feel better from muscle pain. The epsom salt and peppermint oils help cool down your muscles and make you feel better.''', 
'''Both turmeric and ginger contain compounds with anti-inflammatory properties, and ginger has been shown to reduce muscle pain and soreness in some studies. This recipe combines these two ingredients with chicken and vegetables for a healthy and flavorful meal that may help with muscle pain.''']




