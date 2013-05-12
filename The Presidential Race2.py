# Howdy ya'll!
# Thank you for looking at my AMAZING(ly crappy) game!
# To learn more about the game background, please visit
# this link: http://n00bc0d3r.blogspot.com/2013/05/give-me-suggestions.html
# 
# This is a simple text-based game that uses a 20-sided die.
# If you do not have a 20-sided die, visit the website below to emulate one:
# http://www.roll-dice-online.com/
# In the first box chose 20, and in the following boxes chose '1', and click
# on 'Roll dice' to roll each time. Then, enter that number into the game.
# 
# PLEASE submit feedback / compliments / insults / marriage proposals to
# the comment of the above-mentioned blog (line 4).
# 
# Enjoy!

from random import randint
health = 100

def encounter1(enemies, enhealthstart, health):
	enhealth = enhealthstart
	while health > 0 and enemies > 0:
		while enhealth > 0 and health > 0:
			print '\n\nYour health is at ' + `health` + ' and the enemy in front of you has ' + `enhealth` + ' health.\nRoll the dice and enter the value to attack. \ntype "Random" to generate a roll, or "Heal" to heal.'
			hit = raw_input('>>')
			if str(hit).lower() == 'random':
				hit = randint(1,20)
			elif str(hit).lower() == 'heal':
				print '\nYou take a swig of Canady Dry ginger-ale, which restores your health from ' + `health` + ' to ' + `(health+15)` + '.'
				health = health + 15
			elif hit == 1:
				print '\nYour Canadian instinct takes over and you stand around mumbling "sorry" and "eh" a lot.. the enemy takes no damage.'
			elif hit <= 6:
				print '\nYou trot around your enemy, giving them a few light kicks. Their health is now at ' + `(enhealth-int(hit))` + '.'
				enhealth = enhealth - int(hit)
			elif hit <=12:
				print '\nMaple-syrup spray! You blast a stream of hot syrup at your enemy.\nTheir health is now ' + `(enhealth - int(hit))` + '.'
				enhealth = enhealth - int(hit)
			elif hit <=19:
				print '\nYou summon a tempest of maple-leaves, which encircles your enemy, giving them thousands of paper-cuts! \nYour enemy\'s health is now at ' + `(enhealth - int(hit))` + '.'
				enhealth = enhealth - int(hit)
			elif hit == 20:
				print '\nPATRIOTIC OVERLOAD. You transform into a mighty moose temporarily, trampling your enemy into the ground, utterly destroying them!!'
				enhealth = 0

			else:
				print '\nWhat? That\'s not a valid input. I guess you want to skip your turn, sucka!\nThe enemy takes no damage!'
	
		if enhealth > 0:		
			enhit = randint(1,20)
			if enhit == 1:
				print 'Your opponent stumbles on their roller-blades, throughly embarased.\nYou take no damage.'
			elif enhit <= 6:
				print 'Your enemy skates around you in circles, slapping you with "Vote Drag-Shark" stickers.\nYou take ' + `enhit` + ' damage and your health is now ' + `(health-enhit)` + '.\n'
				health = health - enhit
			elif enhit <=12:
				print 'The enemy resorts to violence, skating over your freshly-shined hooves! \nYou take ' + `enhit` + ' damage, and your health is now ' + `(health - enhit)` + '.\n'
				health = health - enhit
			elif enhit <=19:
				print 'The enemy throws low-quality cupcake ingredients at you.. how it burns your skin!!!\nOuch.. you were hit for ' + `enhit` + ' points. You now have ' + `(health - enhit)` + ' health.\n'
				health = health - enhit
			elif enhit == 20:
				print 'RIGHT IN THE FAMILY JEWELS! Your enemy slap-shots a hockey puck into your... ahhem...\nYou were hit for ' + `enhit` + ' points.You now have ' + `(health - enhit)` + ' health.\n'
				health = health - 30
	
		if enhealth <= 0:
			print 'The enemy falls to the ground, overwhelmed by your patriotism.\n'
			enemies = enemies - 1
			if enemies > 0:
				print 'A new enemy steps forward with full health!\n\n'
				enhealth = enhealthstart
encounter1(2, 30, health)
saidfaf=input('Press Enter to close.')