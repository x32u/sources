from discord.ext import commands


async def create_db(self: commands.Bot):

    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS prefixes (guild_id BIGINT, prefix TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS selfprefix (user_id BIGINT, prefix TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS nodata (user_id BIGINT, state TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS snipe (guild_id BIGINT, channel_id BIGINT, author TEXT, content TEXT, attachment TEXT, avatar TEXT, time TIMESTAMPTZ)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS afk (guild_id BIGINT, user_id BIGINT, reason TEXT, time INTEGER);"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS voicemaster (guild_id BIGINT, channel_id BIGINT, interface BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS vcs (user_id BIGINT, voice BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS fake_permissions (guild_id BIGINT, role_id BIGINT, permissions TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS confess (guild_id BIGINT, channel_id BIGINT, confession INTEGER);"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS marry (author BIGINT, soulmate BIGINT, time INTEGER)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS mediaonly (guild_id BIGINT, channel_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS tickets (guild_id BIGINT, message TEXT, channel_id BIGINT, category BIGINT, color INTEGER, logs BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS opened_tickets (guild_id BIGINT, channel_id BIGINT, user_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS ticket_topics (guild_id BIGINT, name TEXT, description TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS ticket_support (guild_id BIGINT, role_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS pingonjoin (channel_id BIGINT, guild_id BIGINT);"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS autorole (role_id BIGINT, guild_id BIGINT);"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS levels (guild_id BIGINT, author_id BIGINT, exp INTEGER, level INTEGER, total_xp INTEGER)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS levelsetup (guild_id BIGINT, channel_id BIGINT, destination TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS levelroles (guild_id BIGINT, level INTEGER, role_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS oldusernames (username TEXT, discriminator TEXT, time INTEGER, user_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS donor (user_id BIGINT, time INTEGER);"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS restore (guild_id BIGINT, user_id BIGINT, roles TEXT);"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS lastfm (user_id BIGINT, username TEXT);"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS lastfmcc (user_id BIGINT, command TEXT);"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS lfmode (user_id BIGINT, mode TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS lfcrowns (user_id BIGINT, artist TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS lfreactions (user_id BIGINT, reactions TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS starboardmes (guild_id BIGINT, channel_starboard_id BIGINT, channel_message_id BIGINT, message_starboard_id BIGINT, message_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS starboard (guild_id BIGINT, channel_id BIGINT, count INTEGER, emoji_id BIGINT, emoji_text TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS seen (guild_id BIGINT, user_id BIGINT, time INTEGER);"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS booster_module (guild_id BIGINT, base BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS booster_roles (guild_id BIGINT, user_id BIGINT, role_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS hardban (guild_id BIGINT, banned BIGINT, author BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS forcenick (guild_id BIGINT, user_id BIGINT, nickname TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS uwulock (guild_id BIGINT, user_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS shutup (guild_id BIGINT, user_id BIGINT)"
    )
    await self.db.execute("CREATE TABLE IF NOT EXISTS antiinvite (guild_id BIGINT)")
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS whitelist (guild_id BIGINT, module TEXT, object_id BIGINT, mode TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS invoke (guild_id BIGINT, command TEXT, embed TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS chatfilter (guild_id BIGINT, word TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS autoreact (guild_id BIGINT, trigger TEXT, emojis TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS welcome (guild_id BIGINT, channel_id BIGINT, mes TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS leave (guild_id BIGINT, channel_id BIGINT, mes TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS boost (guild_id BIGINT, channel_id BIGINT, mes TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS antiraid (guild_id BIGINT, command TEXT, punishment TEXT, seconds INTEGER)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS disablecommand (guild_id BIGINT, command TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS reactionrole (guild_id BIGINT, message_id BIGINT, channel_id BIGINT, role_id BIGINT, emoji_id BIGINT, emoji_text TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS editsnipe (guild_id BIGINT, channel_id BIGINT, author_name TEXT, author_avatar TEXT, before_content TEXT, after_content TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS reactionsnipe (guild_id BIGINT, channel_id BIGINT, author_name TEXT, author_avatar TEXT, emoji_name TEXT, emoji_url TEXT, message_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS mod (guild_id BIGINT, channel_id BIGINT, jail_id BIGINT, role_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS cases (guild_id BIGINT, count INTEGER)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS warns (guild_id BIGINT, user_id BIGINT, author_id BIGINT, time TEXT, reason TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS jail (guild_id BIGINT, user_id BIGINT, roles TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS error (code TEXT, error TEXT, guild_id BIGINT, user_id BIGINT, command TEXT, channel BIGINT, time INTEGER)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS joint (guild_id BIGINT, hits INTEGER, holder BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS counters (guild_id BIGINT, channel_type TEXT, channel_id BIGINT, channel_name TEXT, module TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS bumps (guild_id BIGINT, bool TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS boosterslost (guild_id BIGINT, user_id BIGINT, time INTEGER)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS dm (guild_id BIGINT, command TEXT, embed TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS discrim (guild_id BIGINT, role_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS joindm (guild_id BIGINT, message TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS birthday (user_id BIGINT, bday TIMESTAMPTZ, said TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS antispam (guild_id BIGINT, seconds INTEGER, count INTEGER, punishment TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS timezone (user_id BIGINT, zone TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS webhook (guild_id BIGINT, channel_id BIGINT, code TEXT, url TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS naughtycorner (guild_id BIGINT, channel_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS naughtycorner_members (guild_id BIGINT, user_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS confess_members (guild_id BIGINT, user_id BIGINT, confession INTEGER)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS confess_mute (guild_id BIGINT, user_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS antinuke_toggle (guild_id BIGINT, logs BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS antinuke_whitelist (guild_id BIGINT, user_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS antinuke_admins (guild_id BIGINT, user_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS antinuke (guild_id BIGINT, module TEXT, punishment TEXT, threshold INTEGER)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS giveaway (guild_id BIGINT, channel_id BIGINT, message_id BIGINT, winners INTEGER, members TEXT, finish TIMESTAMPTZ, host BIGINT, title TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS gw_ended (channel_id BIGINT, message_id BIGINT, members TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS diary (user_id BIGINT, text TEXT, title TEXT, date TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS reskin (user_id BIGINT, toggled BOOL, name TEXT, avatar TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS vanity (guild_id BIGINT, vanity_message TEXT, vanity_string TEXT, role_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS autoresponses (guild_id BIGINT, key TEXT, response TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS settings_prefix (guild_id BIGINT, toggled BOOLEAN)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS settings_social (guild_id BIGINT, toggled BOOLEAN,  prefix TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS skullboardmes (guild_id BIGINT, channel_starboard_id BIGINT, channel_message_id BIGINT, message_starboard_id BIGINT, message_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS skullboard (guild_id BIGINT, channel_id BIGINT, count INTEGER, emoji_id BIGINT, emoji_text TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS autokick (guild_id BIGINT, autokick_users BIGINT, author BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS private (guild_id BIGINT, user_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS autopfp (guild_id BIGINT, channel_id BIGINT, genre TEXT, type TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS autobanner (guild_id BIGINT, channel_id BIGINT, genre TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS sticky (guild_id BIGINT, channel_id BIGINT, key TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS stickymessage (guild_id BIGINT, channel_id BIGINT, message_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS restrictcommand (guild_id BIGINT, command TEXT, role_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS authorize (guild_id BIGINT, buyer BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS stickym (guild_id BIGINT, channel_id BIGINT, key TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS reminder (author_id BIGINT, channel_id BIGINT, guild_id BIGINT, time TEXT, task TEXT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS member_logs(guild_id BIGINT, channel_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS voice_logs(guild_id BIGINT, channel_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS server_logs(guild_id BIGINT, channel_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS message_logs(guild_id BIGINT, channel_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS channel_logs(guild_id BIGINT, channel_id BIGINT)"
    )
    await self.db.execute(
        "CREATE TABLE IF NOT EXISTS role_logs(guild_id BIGINT, channel_id BIGINT)"
    )
