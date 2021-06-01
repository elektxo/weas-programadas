const say = require('say');

const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
	console.log('Bot is ready!');
});

client.on('message', message => {
	// Receiving the message
	console.log(message.content);
	if (message.content === 'amorcito') {
		message.reply('chiii aracheli es un amor :)');
	}

	if (message.content === 'quien es la mas bella del server?') {
		message.reply('ambos sabemos la respuesta, aracheli nuestra rubia es la mas sexy, hermona y adora');
	}

	if (message.content === 'hola') {
		message.reply(`hola ${message.author}!`);
		say.speak('Hello');
	}

	if (message.content.includes('¡')){
		message.channel.send(say.speak(message.content));
	}
});

client.login('ODIwMjQ4NDE3NjE1NzQwOTM5.YEyZ3g.ZHvTnRMkkcXj0bKRhliyNu2_sa8')
