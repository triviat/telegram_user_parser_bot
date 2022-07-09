# telegram_user_parser_bot
Telegram user-bot for parsing channel/chats with custom filters.
<hr>
<p>Install dependencies first (write to console): <code>pip install telethon aiohttp</code></p>

<p>To start working with the bot, you need to set up the keywords that the bot wdill use to filter messages coming from channels and chats.
Keywords can be written to files <b>white_list.txt</b> and <b>black_list.txt</b></p>

<p>After configuration, you can run file <b>main.py</b> with command <code>python main.py</code></p>
<p>When you first start the bot, to manage your telegram account, it will ask for a phone number, password and confirmation code. The confirmation code will come in the telegram itself.</p>
<p>After successful login, file <b>user.session</b> will be created in the directory with the project. With this file, when restarting the bot, you will not have to re-enter all the data, it has already saved them.</p>
