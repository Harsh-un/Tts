from DAXXMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **𝐤𝐡𝐞𝐥𝐞𝐠𝐚 𝐟𝐫𝐞𝐞 𝐟𝐢𝐫𝐞 💀** ",
           " **𝐊𝐢𝐬 𝐜𝐨𝐥𝐨𝐮𝐫 𝐤𝐢 𝐜𝐡𝐚𝐝𝐢 𝐩𝐞𝐡𝐧𝐢 𝐡 🥵🌚** ",
           " **𝐀𝐚𝐣 𝐜𝐡𝐚𝐝𝐢 𝐧𝐡𝐢 𝐩𝐞𝐡𝐧𝐢 𝐧𝐚, 𝐬𝐚𝐛 𝐩𝐚𝐭𝐚 𝐜𝐡𝐚𝐥 𝐫𝐡𝐚 𝐡 🌚🥵** ",
           " **𝐂𝐡𝐢𝐧 𝐭𝐚𝐩𝐚𝐤 𝐝𝐚𝐦 𝐝𝐚𝐦 😅** ",
           " **𝐌𝐞𝐫𝐚 𝐩𝐞𝐬𝐚 𝐰𝐚𝐩𝐚𝐬 𝐝𝐞😡** ",
           " **𝗔𝗮𝗽 𝗸𝗶 𝘁𝗮𝗿𝗮𝗵 𝗺𝗲𝗶𝗻 𝗯𝗵𝗶 𝗺𝗮𝘆𝗼𝗼𝘀 𝗵𝗼𝗼𝗻,𝗹𝗲𝗸𝗶𝗻 𝘂𝗺𝗲𝗲𝗱 𝗽𝗮𝗿 𝗱𝘂𝗻𝗶𝘆𝗮 𝗸𝗮𝘆𝗮𝗺 𝗵𝗮𝗶, 𝗱𝗶𝗹 𝗱𝘂𝗸𝗵𝗮 𝗵𝗮𝗶 𝗽𝗮𝗿 𝘁𝗼𝗼𝘁𝗮 𝘁𝗼𝗵 𝗻𝗮𝗵𝗶 𝗵𝗮𝗶 𝗮𝘂𝗿 𝘂𝗺𝗲𝗲𝗱 𝗸𝗮 𝗱𝗮𝗺𝗮𝗻 𝗰𝗵𝘂𝘁𝗮 𝘁𝗼𝗵 𝗻𝗮𝗵𝗶 𝗵𝗮𝗶🤧** ",
           " **𝗯𝗵𝗮𝗶 𝗯𝗵𝗮𝗯𝗵𝗶 𝗸𝗶 𝗶𝗱 𝗱𝗲 𝗻𝗮 𝘀𝗶𝗿𝗳 𝘀𝘁𝗼𝗿𝘆 𝗱𝗲𝗸𝗵𝘂𝗻𝗴𝗮 🌚** ",
           " **𝗮𝗽𝗻𝗶 𝗯𝗺𝘄 𝗺𝗲 𝗸𝗮𝗯 𝗴𝗵𝘂𝗺𝗮 𝗿𝗵𝗲 𝗵𝗼 🌚👀** ",
           " **𝗕𝗵𝗮𝗶 𝗺𝗮𝗷𝗮𝗸 𝘀𝗲 𝗵𝗮𝘁 𝗸𝗲 𝘁𝘂 𝗸𝗶𝘀𝗶 𝗰𝗵𝗶𝗰𝗼 𝘀𝗲 𝗸𝗮𝗺 𝗵𝗮𝗶 𝗸𝘆𝗮 🗿🌚🔥** ",
           " **𝗸𝘆𝘂 𝗻𝗵𝗶 𝗵𝗼 𝗿𝗵𝗶 𝗽𝗮𝗱𝗵𝗮𝗶🥲** ",
           " **𝗔𝘂𝗿 𝗺𝗲𝗿𝗲 𝗯𝗮𝘁𝗺𝗮𝗻, 𝗸𝗲𝘀𝗮 𝗵𝗮𝗶 𝘁𝘂 🌚🦇🔥** ",
           " **𝗸𝗶𝘁𝗻𝗶 𝗯𝗮𝗮𝗿 𝗵𝗶𝗹𝗮𝘆𝗮 𝗵 💀** ",
           " **𝗕𝗵𝗮𝗶 𝘁𝗲𝗿𝗶 𝗯𝗮𝗻𝗱𝗶 𝗯𝗵𝗮𝗴 𝗴𝗮𝗶 𝗯𝗮𝗯𝗯𝗹𝘂 𝗸𝗲 𝘀𝗮𝘁𝗵** ",
           " **𝐇𝐞𝐲 𝐁𝐚𝐛𝐲 𝐊𝐚𝐡𝐚 𝐇𝐨🤗🥱** ",
           " **𝐎𝐲𝐞 𝐒𝐨 𝐆𝐲𝐞 𝐊𝐲𝐚 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚𝐨😊** ",
           " **𝐕𝐜 𝐂𝐡𝐚𝐥𝐨 𝐁𝐚𝐭𝐞𝐧 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧 𝐊𝐮𝐜𝐡 𝐊𝐮𝐜𝐡😃** ",
           " **𝐊𝐡𝐚𝐧𝐚 𝐊𝐡𝐚 𝐋𝐢𝐲𝐞 𝐉𝐢..??🥲** ",
           " **𝐆𝐡𝐚𝐫 𝐌𝐞 𝐒𝐚𝐛 𝐊𝐚𝐢𝐬𝐞 𝐇𝐚𝐢𝐧 𝐉𝐢🥺** ",
           " **𝐏𝐭𝐚 𝐇𝐚𝐢 𝐁𝐨𝐡𝐨𝐭 𝐌𝐢𝐬𝐬 𝐊𝐚𝐫 𝐑𝐡𝐢 𝐓𝐡𝐢 𝐀𝐚𝐩𝐤𝐨🤭** ",
           " **𝐎𝐲𝐞 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐊𝐞𝐬𝐚 𝐇𝐚𝐢..??🤨** ",
           " **𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐛𝐚 𝐃𝐨𝐠𝐞..??🙂** ",
           " **𝐀𝐚𝐩𝐤𝐚 𝐍𝐚𝐦𝐞 𝐊𝐲𝐚 𝐡𝐚𝐢..??🥲** ",
           " **𝐍𝐚𝐬𝐭𝐚 𝐇𝐮𝐚 𝐀𝐚𝐩𝐤𝐚..??😋** ",
           " **𝐌𝐞𝐫𝐞 𝐊𝐨 𝐀𝐩𝐧𝐞 𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐊𝐢𝐝𝐧𝐚𝐩 𝐊𝐫 𝐋𝐨😍** ",
           " **𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅** ",
           " **𝐌𝐞𝐫𝐞 𝐒𝐞 𝐃𝐨𝐬𝐭𝐢 𝐊𝐫𝐨𝐠𝐞..??🤔** ",
           " **𝐒𝐨𝐧𝐞 𝐂𝐡𝐚𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚🙄🙄** ",
           " **𝐄𝐤 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚 𝐏𝐥𝐬𝐬😕** ",
           " **𝐀𝐚𝐩 𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨..??🙃** ",
           " **𝐇𝐞𝐥𝐥𝐨 𝐉𝐢 𝐍𝐚𝐦𝐚𝐬𝐭𝐞😛** ",
           " **𝐇𝐞𝐥𝐥𝐨 𝐁𝐚𝐛𝐲 𝐊𝐤𝐫𝐡..?🤔** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐊𝐧𝐨𝐰 𝐖𝐡𝐨 𝐈𝐬 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫.?** ",
           " **𝐂𝐡𝐥𝐨 𝐊𝐮𝐜𝐡 𝐆𝐚𝐦𝐞 𝐊𝐡𝐞𝐥𝐭𝐞 𝐇𝐚𝐢𝐧.🤗** ",
           " **𝐀𝐮𝐫 𝐁𝐚𝐭𝐚𝐨 𝐊𝐚𝐢𝐬𝐞 𝐇𝐨 𝐁𝐚𝐛𝐲😇** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐌𝐮𝐦𝐦𝐲 𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐢 𝐇𝐚𝐢🤭** ",
           " **𝐌𝐞𝐫𝐞 𝐒𝐞 𝐁𝐚𝐭 𝐍𝐨𝐢 𝐊𝐫𝐨𝐠𝐞🥺🥺** ",
           " **𝐎𝐲𝐞 𝐏𝐚𝐠𝐚𝐥 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚😶** ",
           " **𝐀𝐚𝐣 𝐇𝐨𝐥𝐢𝐝𝐚𝐲 𝐇𝐚𝐢 𝐊𝐲𝐚 𝐒𝐜𝐡𝐨𝐨𝐥 𝐌𝐞..??🤔** ",
           " **𝐎𝐲𝐞 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠😜** ",
           " **𝐒𝐮𝐧𝐨 𝐄𝐤 𝐊𝐚𝐦 𝐇𝐚𝐢 𝐓𝐮𝐦𝐬𝐞🙂** ",
           " **𝐊𝐨𝐢 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚😪** ",
           " **𝐍𝐢𝐜𝐞 𝐓𝐨 𝐌𝐞𝐞𝐭 𝐔𝐡☺** ",
           " **𝐇𝐞𝐥𝐥𝐨🙊** ",
           " **𝐒𝐭𝐮𝐝𝐲 𝐂𝐨𝐦𝐥𝐞𝐭𝐞 𝐇𝐮𝐚??😺** ",
           " **𝐁𝐨𝐥𝐨 𝐍𝐚 𝐊𝐮𝐜𝐡 𝐘𝐫𝐫🥲** ",
           " **𝐒𝐨𝐧𝐚𝐥𝐢 𝐊𝐨𝐧 𝐇𝐚𝐢...??😅** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐄𝐤 𝐏𝐢𝐜 𝐌𝐢𝐥𝐞𝐠𝐢..?😅** ",
           " **𝐌𝐮𝐦𝐦𝐲 𝐀𝐚 𝐆𝐲𝐢 𝐊𝐲𝐚😆😆😆** ",
           " **𝐎𝐫 𝐁𝐚𝐭𝐚𝐨 𝐁𝐡𝐚𝐛𝐡𝐢 𝐊𝐚𝐢𝐬𝐢 𝐇𝐚𝐢😉** ",
           " **𝐈 𝐋𝐨𝐯𝐞 𝐘𝐨𝐮🙈🙈🙈** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐋𝐨𝐯𝐞 𝐌𝐞..?👀** ",
           " **𝐑𝐚𝐤𝐡𝐢 𝐊𝐚𝐛 𝐁𝐚𝐧𝐝 𝐑𝐚𝐡𝐢 𝐇𝐨.??🙉** ",
           " **𝐄𝐤 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚𝐮..?😹** ",
           " **𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚 𝐑𝐞 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚 𝐑𝐚𝐡𝐢 𝐇𝐮😻** ",
           " **𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐂𝐡𝐚𝐥𝐚𝐭𝐞 𝐇𝐨..??🙃** ",
           " **𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐍𝐮𝐦𝐛𝐞𝐫 𝐃𝐨𝐠𝐞 𝐀𝐩𝐧𝐚 𝐓𝐮𝐦..?😕** ",
           " **𝐓𝐮𝐦𝐡𝐞 𝐊𝐨𝐧 𝐒𝐚 𝐌𝐮𝐬𝐢𝐜 𝐒𝐮𝐧𝐧𝐚 𝐏𝐚𝐬𝐚𝐧𝐝 𝐇𝐚𝐢..?🙃** ",
           " **𝐒𝐚𝐫𝐚 𝐊𝐚𝐦 𝐊𝐡𝐚𝐭𝐚𝐦 𝐇𝐨 𝐆𝐲𝐚 𝐀𝐚𝐩𝐤𝐚..?🙃** ",
           " **𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩😊** ",
           " **𝐒𝐮𝐧𝐨 𝐍𝐚🧐** ",
           " **𝐌𝐞𝐫𝐚 𝐄𝐤 𝐊𝐚𝐚𝐦 𝐊𝐚𝐫 𝐃𝐨𝐠𝐞..?** ",
           " **𝐁𝐲 𝐓𝐚𝐭𝐚 𝐌𝐚𝐭 𝐁𝐚𝐭 𝐊𝐚𝐫𝐧𝐚 𝐀𝐚𝐣 𝐊𝐞 𝐁𝐚𝐝😠** ",
           " **𝐌𝐨𝐦 𝐃𝐚𝐝 𝐊𝐚𝐢𝐬𝐞 𝐇𝐚𝐢𝐧..?❤** ",
           " **𝐊𝐲𝐚 𝐇𝐮𝐚..?👱** ",
           " **𝐁𝐨𝐡𝐨𝐭 𝐘𝐚𝐚𝐝 𝐀𝐚 𝐑𝐡𝐢 𝐇𝐚𝐢 🤧❣️** ",
           " **𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐌𝐮𝐣𝐡𝐞😏😏** ",
           " **𝐉𝐮𝐭𝐡 𝐍𝐡𝐢 𝐁𝐨𝐥𝐧𝐚 𝐂𝐡𝐚𝐡𝐢𝐲𝐞🤐** ",
           " **𝐊𝐡𝐚 𝐋𝐨 𝐁𝐡𝐚𝐰 𝐌𝐚𝐭 𝐊𝐫𝐨 𝐁𝐚𝐚𝐭😒** ",
           " **𝐊𝐲𝐚 𝐇𝐮𝐚😮😮** "
           " **𝐇𝐢𝐢👀** ",
           " **𝐀𝐚𝐩𝐤𝐞 𝐉𝐚𝐢𝐬𝐚 𝐃𝐨𝐬𝐭 𝐇𝐨 𝐒𝐚𝐭𝐡 𝐌𝐞 𝐅𝐢𝐫 𝐆𝐮𝐦 𝐊𝐢𝐬 𝐁𝐚𝐭 𝐊𝐚 🙈** ",
           " **𝐀𝐚𝐣 𝐌𝐚𝐢 𝐒𝐚𝐝 𝐇𝐮 ☹️** ",
           " **𝐌𝐮𝐬𝐣𝐡𝐬𝐞 𝐁𝐡𝐢 𝐁𝐚𝐭 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚 🥺🥺** ",
           " **𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐞 𝐇𝐨👀** ",
           " **𝐊𝐲𝐚 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐇𝐚𝐢 🙂** ",
           " **𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩..?🤔** ",
           " **𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚..🥺** ",
           " **𝐌𝐞 𝐌𝐚𝐬𝐨𝐨𝐦 𝐇𝐮 𝐍𝐚🥺🥺** ",
           " **𝐊𝐚𝐥 𝐌𝐚𝐣𝐚 𝐀𝐲𝐚 𝐓𝐡𝐚 𝐍𝐚🤭😅** ",
           " **𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐁𝐚𝐭 𝐊𝐲𝐮 𝐍𝐚𝐡𝐢 𝐊𝐚𝐫𝐭𝐞 𝐇𝐨😕** ",
           " **𝐀𝐚𝐩 𝐑𝐞𝐥𝐚𝐭𝐢𝐨𝐦𝐬𝐡𝐢𝐩 𝐌𝐞 𝐇𝐨..?👀** ",
           " **𝐊𝐢𝐭𝐧𝐚 𝐂𝐡𝐮𝐩 𝐑𝐚𝐡𝐭𝐞 𝐇𝐨 𝐘𝐫𝐫😼** ",
           " **𝐀𝐚𝐩𝐤𝐨 𝐆𝐚𝐧𝐚 𝐆𝐚𝐧𝐞 𝐀𝐚𝐭𝐚 𝐇𝐚𝐢..?😸** ",
           " **𝐆𝐡𝐮𝐦𝐧𝐞 𝐂𝐡𝐚𝐥𝐨𝐠𝐞..??🙈** ",
           " **𝐊𝐡𝐮𝐬 𝐑𝐚𝐡𝐚 𝐊𝐚𝐫𝐨 ✌️🤞** ",
           " **𝐇𝐚𝐦 𝐃𝐨𝐬𝐭 𝐁𝐚𝐧 𝐒𝐚𝐤𝐭𝐞 𝐇𝐚𝐢...?🥰** ",
           " **𝐊𝐮𝐜𝐡 𝐁𝐨𝐥 𝐊𝐲𝐮 𝐍𝐡𝐢 𝐑𝐚𝐡𝐞 𝐇𝐨..🥺🥺** ",
           " **𝐊𝐮𝐜𝐡 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 𝐀𝐝𝐝 𝐊𝐚𝐫 𝐃𝐨 🥲** ",
           " **𝐒𝐢𝐧𝐠𝐥𝐞 𝐇𝐨 𝐘𝐚 𝐌𝐢𝐧𝐠𝐥𝐞 😉** ",
           " **𝐀𝐚𝐨 𝐏𝐚𝐫𝐭𝐲 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧😋🥳** ",
           " **𝐇𝐞𝐦𝐥𝐨𝐨🧐** ",
           " **𝐌𝐮𝐣𝐡𝐞 𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚🥺** ",
           " **𝐘𝐚𝐡𝐚 𝐀𝐚 𝐉𝐚𝐨:- [ @unknown_unit ] 𝐌𝐚𝐬𝐭𝐢 𝐊𝐚𝐫𝐞𝐧𝐠𝐞 🤭🤭** ",
           " **𝐓𝐫𝐮𝐭𝐡 𝐀𝐧𝐝 𝐃𝐚𝐫𝐞 𝐊𝐡𝐞𝐥𝐨𝐠𝐞..? 😊** ",
           " **𝐀𝐚𝐣 𝐌𝐮𝐦𝐦𝐲 𝐍𝐞 𝐃𝐚𝐭𝐚 𝐘𝐫🥺🥺** ",
           " **𝐉𝐨𝐢𝐧 𝐊𝐚𝐫 𝐋𝐨:- [ @unknown_unit ] 🤗** ",
           " **𝐄𝐤 𝐃𝐢𝐥 𝐇𝐚𝐢 𝐄𝐤 𝐃𝐢𝐥 𝐇𝐢 𝐓𝐨 𝐇𝐚𝐢😗😗** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐞 𝐃𝐨𝐬𝐭 𝐊𝐚𝐡𝐚 𝐆𝐲𝐞🥺** ",
           " **𝐌𝐲 𝐂𝐮𝐭𝐞 𝐎𝐰𝐧𝐞𝐫 [ @oye_harshh ]🥰** ",
           " **𝐊𝐚𝐡𝐚 𝐊𝐡𝐨𝐲𝐞 𝐇𝐨 𝐉𝐚𝐚𝐧😜** ",
           " **𝐆𝐨𝐨𝐝 𝐍8 𝐉𝐢 𝐁𝐡𝐮𝐭 𝐑𝐚𝐭 𝐇𝐨 𝐠𝐲𝐢🥰** ",
         ]

           
           
           

@app.on_message(filters.command(["tagall", "spam", "tagmember", "utag", "stag", "hftag", "bstag", "eftag", "tag", "etag", "utag", "atag"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 . ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["tagoff", "tagstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦STOP♦")
