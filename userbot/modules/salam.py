from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`𝘼𝙨𝙨𝙖𝙡𝙖𝙢𝙪𝙖𝙡𝙖𝙞𝙠𝙪𝙢 𝙮𝙖 𝙖𝙝𝙡𝙞 𝙠𝙪𝙗𝙪𝙧!!`")


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`𝘼𝙨𝙨𝙖𝙡𝙖𝙢𝙪𝙖𝙡𝙖𝙞𝙠𝙪𝙢 𝙮𝙖 𝙖𝙝𝙡𝙞 𝙠𝙪𝙗𝙪𝙧!!`")


@register(outgoing=True, pattern='^.L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`𝙒𝙖𝙖𝙡𝙖𝙞𝙠𝙪𝙢𝙨𝙖𝙡𝙖𝙢 𝙮𝙖 𝙖𝙝𝙡𝙞 𝙠𝙪𝙗𝙪𝙧!!`")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`𝙒𝙖𝙖𝙡𝙖𝙞𝙠𝙪𝙢𝙨𝙖𝙡𝙖𝙢 𝙮𝙖 𝙖𝙝𝙡𝙞 𝙠𝙪𝙗𝙪𝙧!!`")


CMD_HELP.update({
    "salam":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.P` | `.p`\
\n↳ : Untuk Memberi salam.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.L` `.l`\
\n↳ : Untuk Menjawab Salam."
})
