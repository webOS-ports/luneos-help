"""Redrawn help artwork: flat SVG versions of the webOS toolbar glyphs and device drawings."""
import re

S = 'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
F = 'fill="currentColor"'
G = {
 "bookmark": f'<path {S} d="M7 4h10v16l-5-4-5 4z"/>',
 "bookmark-add": f'<path {S} d="M6 6h7v14l-3.5-3L6 20zM17 3v6M14 6h6"/>',
 "directions": f'<path {S} d="M12 3l9 9-9 9-9-9zM9 14v-2.5A1.5 1.5 0 0 1 10.5 10H15M13 7.5 15.5 10 13 12.5"/>',
 "warn": f'<path {S} d="M12 4 22 20H2zM12 10v5"/><circle cx="12" cy="17.6" r="1" {F}/>',
 "pencil": f'<path {S} d="M4 20l1-5L16 4l4 4L9 19zM14 6l4 4"/>',
 "pin": f'<path {F} d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.500a2.500 2.500 0 0 1 0 5z"/>',
 "play": f'<path {F} d="M8 5l12 7-12 7z"/>',
 "pause": f'<path {F} d="M7 5h4v14H7zM13 5h4v14h-4z"/>',
 "bell": f'<path {S} d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4zM10 21h4"/>',
 "send": f'<path {S} d="M21 3 3 10l7 3 3 8zM10 13l5-5"/>',
 "share": f'<path {S} d="M11 5H5v14h14v-6M13 4h7v7M20 4l-9 9"/>',
 "lines": f'<path {S} d="M4 6h16M4 12h16M4 18h16"/>',
 "contact": f'<rect x="3" y="5" width="18" height="14" rx="2" {S}/><circle cx="9" cy="11" r="2" {S}/><path {S} d="M5.500 16.500c.7-1.800 6.300-1.800 7 0M15 10h3M15 14h3"/>',
 "person": f'<circle cx="12" cy="8" r="4" {S}/><path {S} d="M4 21c1-6 15-6 16 0"/>',
 "person-add": f'<circle cx="10" cy="8" r="4" {S}/><path {S} d="M3 21c1-6 13-6 14 0M19 4v6M16 7h6"/>',
 "people": f'<circle cx="9" cy="8" r="3.500" {S}/><circle cx="17" cy="9" r="2.500" {S}/><path {S} d="M3 20c.8-5 11.200-5 12 0M16 15c2.500-.3 4.500 1 5 4"/>',
 "chat": f'<path {S} d="M4 5h16v11H10l-5 4v-4H4z"/>',
 "star": f'<path {F} d="M12 2.500l2.900 6.300 6.900.8-5.100 4.700 1.400 6.800L12 16.800l-6.100 3.400 1.400-6.800L2.200 9.600l6.900-.8z"/>',
 "info": f'<circle cx="12" cy="12" r="9" {S}/><path {S} d="M12 11v6"/><circle cx="12" cy="7.500" r="1.200" {F}/>',
 "phone": f'<path {F} d="M6.600 3.500 9.800 3l1.700 4.600-2 1.800a12 12 0 0 0 5.100 5.100l1.800-2 4.600 1.700-.5 3.200c-.2 1.100-1.100 1.800-2.200 1.700C10.800 18.800 5.200 13.200 4.900 5.700c-.1-1.100.6-2 1.700-2.200z"/>',
 "hangup": f'<path {F} d="M2 14.500C7 9.500 17 9.500 22 14.500l-1.500 3-4.500-1.500v-2.500c-2.500-.8-5.500-.8-8 0V16l-4.500 1.500z"/>',
 "video": f'<rect x="3" y="7" width="13" height="10" rx="2" {S}/><path {S} d="M16 11l5-3v8l-5-3z"/>',
 "video-off": f'<rect x="3" y="7" width="13" height="10" rx="2" {S}/><path {S} d="M16 11l5-3v8l-5-3zM3 3l18 18"/>',
 "handle": f'<path {S} d="M7 4v16M12 4v16M17 4v16"/>',
 "print": f'<path {S} d="M7 8V3h10v5M6 17H3V9h18v8h-3M7 14h10v7H7z"/>',
 "forward2": f'<path {F} d="M3 5l9 7-9 7zM12 5l9 7-9 7z"/>',
 "lock": f'<rect x="5" y="10" width="14" height="11" rx="2" {S}/><path {S} d="M8 10V7a4 4 0 0 1 8 0v3"/>',
 "target": f'<circle cx="12" cy="12" r="7" {S}/><circle cx="12" cy="12" r="2" {F}/><path {S} d="M12 2v3M12 19v3M2 12h3M19 12h3"/>',
 "map": f'<path {S} d="M3 6l6-2 6 2 6-2v14l-6 2-6-2-6 2zM9 4v14M15 6v14"/>',
 "search": f'<circle cx="10.500" cy="10.500" r="6.500" {S}/><path {S} d="M15.500 15.500 21 21"/>',
 "search-add": f'<circle cx="10.500" cy="10.500" r="6.500" {S}/><path {S} d="M15.500 15.500 21 21M10.500 8v5M8 10.500h5"/>',
 "history": f'<circle cx="12" cy="12" r="9" {S}/><path {S} d="M12 7v5l3.500 2"/>',
 "x": f'<path {S} stroke-width="3" d="M6 6l12 12M18 6 6 18"/>',
 "trash": f'<path {S} d="M4 7h16M9 7V4h6v3M6 7l1 14h10l1-14M10 11v6M14 11v6"/>',
 "folder": f'<path {S} d="M3 7h6l2 2h10v10H3z"/>',
 "folder-move": f'<path {S} d="M3 7h6l2 2h10v10H3zM12 12v5M9.500 14.500 12 12l2.500 2.500"/>',
 "plus": f'<path {S} stroke-width="3" d="M12 5v14M5 12h14"/>',
 "left": f'<path {S} d="M20 12H5M11 6l-6 6 6 6"/>',
 "right": f'<path {S} d="M4 12h15M13 6l6 6-6 6"/>',
 "reply": f'<path {S} d="M10 7 4 12l6 5M4 12h10a6 6 0 0 1 6 6"/>',
 "forward": f'<path {S} d="M14 7l6 5-6 5M20 12H10a6 6 0 0 0-6 6"/>',
 "up": f'<path {S} d="M12 20V5M6 11l6-6 6 6"/>',
 "tri-down": f'<path {F} d="M5 8h14l-7 9z"/>',
 "tri-right": f'<path {F} d="M8 5l10 7-10 7z"/>',
 "tri-left": f'<path {F} d="M16 5 6 12l10 7z"/>',
 "sync": f'<path {S} d="M4 12a8 8 0 0 1 14-5l2 2M20 12a8 8 0 0 1-14 5l-2-2M20 4v5h-5M4 20v-5h5"/>',
 "refresh": f'<path {S} d="M20 12a8 8 0 1 1-2.500-5.800L20 8.500M20 3.500v5h-5"/>',
 "shuffle": f'<path {S} d="M3 7h4l10 10h4M3 17h4l3-3M14 10l3-3h4M18 4l3 3-3 3M18 14l3 3-3 3"/>',
 "attach": f'<path {S} d="M20 11l-8 8a5 5 0 0 1-7-7l9-9a3.500 3.500 0 0 1 5 5l-9 9a2 2 0 0 1-3-3l8-8"/>',
 "flag": f'<path {S} d="M6 21V4h12l-3 4 3 4H6"/>',
 "voicemail": f'<circle cx="7" cy="12" r="4" {S}/><circle cx="17" cy="12" r="4" {S}/><path {S} d="M7 16h10"/>',
 "note": f'<path {S} d="M4 4h16v11l-5 5H4zM20 15h-5v5"/>',
 "headphones": f'<path {S} d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="14" width="4" height="6" rx="1.500" {S}/><rect x="17" y="14" width="4" height="6" rx="1.500" {S}/>',
 "camera": f'<path {S} d="M3 8h4l2-3h6l2 3h4v12H3z"/><circle cx="12" cy="13.500" r="3.500" {S}/>',
 "music-add": f'<path {S} d="M9 18V7l9-2v6"/><circle cx="6.500" cy="18" r="2.500" {S}/><path {S} d="M18 14v6M15 17h6"/>',
 "dialpad": f'<g {F}><circle cx="6" cy="5" r="1.700"/><circle cx="12" cy="5" r="1.700"/><circle cx="18" cy="5" r="1.700"/><circle cx="6" cy="10.500" r="1.700"/><circle cx="12" cy="10.500" r="1.700"/><circle cx="18" cy="10.500" r="1.700"/><circle cx="6" cy="16" r="1.700"/><circle cx="12" cy="16" r="1.700"/><circle cx="18" cy="16" r="1.700"/><circle cx="12" cy="21" r="1.700"/></g>',
 "check": f'<path {S} stroke-width="3" d="M5 13l4.500 4.500L19 7"/>',
 "speaker": f'<path {S} d="M4 9v6h4l5 4V5L8 9zM16.500 9a4 4 0 0 1 0 6M19 6.500a8 8 0 0 1 0 11"/>',
 "mute": f'<path {S} d="M9 5a3 3 0 0 1 6 0v6a3 3 0 0 1-6 0zM5 11a7 7 0 0 0 14 0M12 18v3M3 3l18 18"/>',
 "expand": f'<path {S} d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/>',
 "collapse": f'<path {S} d="M9 4v5H4M15 4v5h5M9 20v-5H4M15 20v-5h5"/>',
 "cal-day": f'<rect x="4" y="5" width="16" height="15" rx="2" {S}/><path {S} d="M4 10h16"/>',
 "cal-week": f'<rect x="4" y="5" width="16" height="15" rx="2" {S}/><path {S} d="M4 10h16M9.300 10v10M14.700 10v10"/>',
 "cal-month": f'<rect x="4" y="5" width="16" height="15" rx="2" {S}/><path {S} d="M4 10h16M4 15h16M9.300 10v10M14.700 10v10"/>',
 "mail": f'<rect x="3" y="5" width="18" height="14" rx="2" {S}/><path {S} d="M3 7l9 7 9-7"/>',
 "car": f'<path {S} d="M4 17v-5l2-6h12l2 6v5zM4 12h16M7 17v2M17 17v2"/>',
 "walk": f'<circle cx="13" cy="4.500" r="2" {S}/><path {S} d="M9 21l3-7-2-3 4-3 2 4h3M12 14l3 3v4M10 11l-3 2"/>',
 "train": f'<rect x="5" y="3" width="14" height="14" rx="3" {S}/><path {S} d="M5 11h14M8 21l2-4M16 21l-2-4"/>',
 "wifi": f'<path {S} d="M3 9a13 13 0 0 1 18 0M6.500 13a8 8 0 0 1 11 0M10 16.500a3 3 0 0 1 4 0"/><circle cx="12" cy="20" r="1.200" {F}/>',
 "hotspot": f'<circle cx="12" cy="11" r="2" {F}/><path {S} d="M8 7a6 6 0 0 0 0 8M16 7a6 6 0 0 1 0 8M5 4a10 10 0 0 0 0 14M19 4a10 10 0 0 1 0 14M12 13v8"/>',
 "doc": f'<path {S} d="M6 3h9l4 4v14H6zM9 12h7M9 16h7"/>',
 "battery": f'<rect x="7" y="4" width="10" height="17" rx="2" {S}/><path {S} d="M10 2h4"/><path {F} d="M9 11h6v8H9z"/>',
 "split": f'<path {S} d="M12 21v-8L6 7M12 13l6-6M4 9V5h4M20 9V5h-4"/>',
 "swap": f'<path {S} d="M4 8h15M15 4l4 4-4 4M20 16H5M9 12l-4 4 4 4"/>',
 "gear": f'<circle cx="12" cy="12" r="3" {S}/><path {S} d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2"/>',
 "record": f'<circle cx="12" cy="12" r="6" {F}/>',
 "stop": f'<rect x="6" y="6" width="12" height="12" rx="2" {F}/>',
 "menu-tap": f'<circle cx="12" cy="12" r="8" {S}/><circle cx="12" cy="12" r="3" {F}/>',
}

# (regex on lower-case file name, glyph, style, plain-language name)
RULES = [
 (r"^web\.png", "map", "round-blue", "Web"), (r"app_catalog", "menu-tap", "btn", "Apps"),
 (r"hw_center", "pill", "key", "Center button"), (r"hw_option|altlock|alt_symbol", "opt", "key", "Option key"),
 (r"hw_sym", "Sym", "key", "Sym key"), (r"hw_shift|keyboard_shift|keyboard_caps", "up", "key", "Shift key"),
 (r"hw_enter", "enter", "key", "Enter key"), (r"hw_space", "space", "key", "Space bar"),
 (r"hw_backspace", "left", "key", "Backspace key"), (r"hw_1", "1", "key", "1 key"),
 (r"keyboard_abc", "ABC", "key", "ABC key"), (r"keyboard_symbol", "+=[]", "key", "Symbols key"),
 (r"titlebar_3g", "3G", "tag", "3G icon"), (r"titlebar_edge", "E", "tag", "EDGE icon"),
 (r"titlebar_gprs", "G", "tag", "GPRS icon"), (r"titlebar_batter", "battery", "plain-green", "Battery icon"),
 (r"important|sendfail", "warn", "plain-amber", "Warning"), (r"drop_pin", "pin", "plain-orange", "Map pin"),
 (r"endcall|ignorecall", "hangup", "round-red", "End call"), (r"answercall|makecall|justtype_call|contacts_phone|messaging_call", "phone", "round-green", "Call"),
 (r"maps_directions", "directions", "btn", "Directions"), (r"maps_customize", "map", "btn", "Map view"),
 (r"maps_currentlocation", "target", "btn", "Current location"), (r"maps_car", "car", "btn", "Driving"),
 (r"maps_walking", "walk", "btn", "Walking"), (r"maps_publictran", "train", "btn", "Public transport"),
 (r"maps_written|maps_results|maps_business", "lines", "btn", "List"), (r"maps_toggle", "swap", "btn", "Switch"),
 (r"web_addbookmark|addbookmark", "bookmark-add", "btn", "Add bookmark"), (r"web_add_search", "search-add", "btn", "Add search"),
 (r"bookmark", "bookmark", "btn", "Bookmarks"), (r"web_viewbook|history", "history", "btn", "History"),
 (r"web_back|maps_back|docview_prev|hw_back", "left", "btn", "Back"), (r"web_forward|maps_forward|docview_next", "right", "btn", "Forward"),
 (r"web_cancel|close_search|cancel|flash_content|launcher_delete|buddies_x|buddy.*x", "x", "round", "Close"),
 (r"web_refresh", "refresh", "btn", "Reload"), (r"web_newbrowser", "plus", "btn", "New card"),
 (r"delete|trash", "trash", "btn", "Delete"), (r"attach", "attach", "btn", "Attachment"),
 (r"print", "print", "btn", "Print"), (r"sms|messaging_send|email_send", "send", "round", "Send"),
 (r"share|photomenu|video_upload", "share", "btn", "Share"), (r"search", "search", "btn", "Search"),
 (r"email_forward", "forward", "btn", "Forward"), (r"reply|messaging_send_", "reply", "btn", "Reply"),
 (r"move_", "folder-move", "btn", "Move to folder"), (r"folder", "folder", "btn", "Folders"),
 (r"openfold|expandb|closefold", "tri-down", "round", "Open"), (r"expand_pane|drag_handles", "handle", "plain", "Drag handle"),
 (r"nextmsg|submenuarr|expand_li", "tri-right", "plain-blue", "Next"), (r"prevmsg", "tri-left", "plain-blue", "Previous"),
 (r"scrollarr|hide_list", "tri-down", "plain", "More"), (r"sync", "sync", "btn", "Sync"),
 (r"shuffle", "shuffle", "btn", "Shuffle"), (r"show_albu", "expand", "btn", "Show album"), (r"show_list", "collapse", "btn", "Show list"),
 (r"voicemail|vvm_new", "voicemail", "btn", "Voicemail"), (r"vvm_vm_gr.*|checkmark|save_edit|vvm", "check", "round", "Done"),
 (r"keypad|dialpad|phone_dial|calendar_month", "dialpad", "btn", "Dial pad"), (r"headset|wiredhead", "headphones", "btn", "Headset"),
 (r"phone_mute|mute_mic", "mute", "btn", "Mute"), (r"turn_off_vid", "video-off", "btn", "Video off"),
 (r"speaker|handset|phone_bluetooth", "speaker", "btn", "Speaker"), (r"sounds", "speaker", "btn", "Sounds"),
 (r"addcall|extract|conference", "split", "btn", "Conference"), (r"swap", "swap", "btn", "Swap calls"),
 (r"calllog|activecal", "person", "btn", "Caller"), (r"favorite|favor|identi|add_fav|addfav", "star", "plain-gold", "Favorite"),
 (r"editcontact|contacts_edit|video_edit", "pencil", "btn", "Edit"), (r"opencontact|contact_detail|openc", "contact", "btn", "Contact details"),
 (r"contacts_create|addphoto|addinfo|email_openc", "person-add", "btn", "Add contact"), (r"contacts_remove", "star", "round", "Remove favorite"),
 (r"buddiesview", "people", "btn", "Buddies"), (r"conversations|messaging_new|messaging_favor|messaging_chang|contacts_send", "chat", "btn", "Conversation"),
 (r"offli", "menu-tap", "round", "Offline"), (r"buddies|messaging_buddi", "check", "round-green", "Online"),
 (r"music_add|add_song", "music-add", "btn", "Add song"), (r"record|video_start", "record", "round-red", "Record"),
 (r"video_stop", "stop", "round-red", "Stop"), (r"pause", "pause", "btn", "Pause"),
 (r"play|preview|ringtone", "play", "round-blue", "Play"), (r"skype_send|video_call|video_save|videos|photosandvideos|camera_video|camera_go", "video", "btn", "Video"),
 (r"camera", "camera", "btn", "Camera"), (r"alarm", "bell", "btn", "Alarm"),
 (r"calendar_day", "cal-day", "btn", "Day view"), (r"calendar_week", "cal-week", "btn", "Week view"),
 (r"memos_email|mail", "mail", "btn", "Email"), (r"memo|task", "note", "btn", "New note"),
 (r"keyguard|lock", "lock", "plain-amber", "Locked"), (r"wifi", "wifi", "round-blue", "Wi-Fi"),
 (r"hot", "hotspot", "btn", "Hotspot"), (r"flag", "flag", "btn", "Flag"),
 (r"quicklaunch|launcher|exhibition", "menu-tap", "btn", "Launcher"), (r"bluetooth", "gear", "btn", "Bluetooth settings"),
 (r"info|details|detail|vpn_edit|edit", "info", "round-blue", "Details"), (r"preference|option", "lines", "btn", "Options"),
 (r"add|new|plus|expand", "plus", "round", "Add"), (r"view|doc|quickoffice", "doc", "btn", "Document"), (r"menu", "menu-tap", "btn", "Menu"),
]

COLOR = {"btn": ("#22344f", "#fff"), "round": ("#22344f", "#fff"), "round-red": ("#d6362f", "#fff"),
         "round-green": ("#3aa53f", "#fff"), "round-blue": ("#1685e8", "#fff"), "plain": (None, "#5b6b85"),
         "plain-blue": (None, "#1685e8"), "plain-green": (None, "#3aa53f"), "plain-amber": (None, "#d99a06"),
         "plain-orange": (None, "#f0771f"), "plain-gold": (None, "#e0a800")}


def lookup(name):
    n = name.lower().replace('"', "")
    for rx, glyph, style, label in RULES:
        if re.search(rx, n):
            return glyph, style, label
    return None


def icon(glyph, style):
    if style == "key":
        body = {"pill": '<rect x="9" y="13.500" width="14" height="5" rx="2.500" fill="#00123a"/>',
                "opt": '<circle cx="16" cy="16" r="4.500" fill="#f0771f"/>',
                "space": '<path d="M9 18v3h14v-3" fill="none" stroke="#00123a" stroke-width="2"/>',
                "enter": '<path d="M23 10v7H10M14 13l-4 4 4 4" fill="none" stroke="#00123a" stroke-width="2.200" stroke-linecap="round" stroke-linejoin="round"/>',
                "up": '<path d="M16 8l7 8h-4v7h-6v-7H9z" fill="#00123a"/>',
                "left": '<path d="M24 16H9M14 10l-6 6 6 6" fill="none" stroke="#00123a" stroke-width="2.200" stroke-linecap="round" stroke-linejoin="round"/>'}.get(glyph)
        wide = 56 if len(glyph) > 3 and glyph not in ("pill", "opt", "space", "enter", "left") else 32
        if body is None:
            body = (f'<text x="{wide/2}" y="21" text-anchor="middle" font-family="Prelude,sans-serif" '
                    f'font-weight="700" font-size="{13 if len(glyph) > 1 else 15}" fill="#00123a">{glyph.replace("&", "&amp;")}</text>')
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {wide} 32"><rect x="1" y="1" width="{wide-2}" height="30" '
                f'rx="7" fill="#fff" stroke="#9fb1ca" stroke-width="1.500"/><rect x="1" y="26" width="{wide-2}" height="5" rx="3" fill="#dbe4f0"/>{body}</svg>')
    if style == "tag":
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#22344f"/>'
                f'<text x="16" y="21" text-anchor="middle" font-family="Prelude,sans-serif" font-weight="700" font-size="14" fill="#fff">{glyph}</text></svg>')
    bg, fg = COLOR[style]
    if bg is None:
        back = ""
    elif style.startswith("round"):
        back = f'<circle cx="16" cy="16" r="15" fill="{bg}"/>'
    else:
        back = f'<rect x="1" y="1" width="30" height="30" rx="8" fill="{bg}"/>'
    scale = 1.33 if bg is None else 0.92
    off = 16 - 12 * scale
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" color="{fg}">{back}'
            f'<g transform="translate({off:.2f} {off:.2f}) scale({scale})">{G[glyph]}</g></svg>')


INK, BLUE, WASH, RULE = "#00123a", "#1685e8", "#eaf4fe", "#9fb1ca"
WALL = '<defs><linearGradient id="w" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b5cc0"/><stop offset="1" stop-color="#00123a"/></linearGradient></defs>'


def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="Prelude,sans-serif">{body}</svg>'


def body_phone(x, y, w, h, keys=False):
    screen = h - (112 if keys else 46)
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26" fill="#fff" stroke="{INK}" stroke-width="3"/>'
    out += f'<rect x="{x+10}" y="{y+22}" width="{w-20}" height="{screen}" rx="6" fill="url(#w)"/>'
    gy = y + 22 + screen + 12
    out += f'<rect x="{x+w/2-16}" y="{gy-2}" width="32" height="6" rx="3" fill="{INK}"/>'
    if keys:
        for r in range(3):
            for c in range(8):
                kw = (w - 28) / 8
                out += f'<rect x="{x+14+c*kw:.1f}" y="{gy+16+r*22}" width="{kw-3:.1f}" height="18" rx="4" fill="{WASH}" stroke="{RULE}"/>'
    return out


def icons_grid(x, y, cols, rows, size, gap):
    colors = ["#ff8a3d", "#42c26b", "#1685e8", "#f4c542", "#e4574f", "#9b7be0"]
    o = ""
    for r in range(rows):
        for c in range(cols):
            o += f'<rect x="{x+c*(size+gap)}" y="{y+r*(size+gap)}" width="{size}" height="{size}" rx="{size*.22:.1f}" fill="{colors[(r*cols+c)%6]}"/>'
    return o


def card(x, y, w, h, tint="#fff"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{tint}" stroke="{RULE}"/>'
            f'<rect x="{x+10}" y="{y+10}" width="{w*.45:.0f}" height="8" rx="4" fill="{RULE}"/>'
            f'<rect x="{x+10}" y="{y+28}" width="{w-20}" height="5" rx="2.500" fill="{WASH}"/>'
            f'<rect x="{x+10}" y="{y+40}" width="{w-20}" height="5" rx="2.500" fill="{WASH}"/>')


def callout(x, y, tx, ty, text):
    return (f'<path d="M{x} {y}L{tx} {ty}" stroke="{BLUE}" stroke-width="1.500"/><circle cx="{x}" cy="{y}" r="3.500" fill="{BLUE}"/>'
            f'<text x="{tx+6}" y="{ty+5}" font-size="14" fill="{INK}">{text}</text>')


def tablet_body(w=420, h=320):
    return (f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="20" fill="#fff" stroke="{INK}" stroke-width="3"/>'
            f'<rect x="28" y="28" width="{w-56}" height="{h-56}" rx="6" fill="url(#w)"/>')


# Numbered drawings: pin numbers and positions follow Palm's originals, so the
# numbered list under each drawing still matches.
def pin(n, x, y, tx, ty, via=None):
    pts = f"M{x} {y}" + (f"L{via[0]} {via[1]}" if via else "") + f"L{tx} {ty}"
    return (f'<path d="{pts}" fill="none" stroke="{BLUE}" stroke-width="2"/><circle cx="{tx}" cy="{ty}" r="3.5" fill="{BLUE}"/>'
            f'<circle cx="{x}" cy="{y}" r="14" fill="#fff" stroke="{INK}" stroke-width="2"/>'
            f'<text x="{x}" y="{y+5.500}" text-anchor="middle" font-size="15" font-weight="700" fill="{INK}">{n}</text>')


def tiles(x, y, cols, rows, size, gap, labels=False):
    pal = ("#ff8a3d", "#42b66e", "#1685e8", "#f2c230", "#e5574f", "#9a7fe0")
    o = ""
    for r in range(rows):
        for c in range(cols):
            o += f'<rect x="{x+c*(size+gap)}" y="{y+r*(size+gap)}" width="{size}" height="{size}" rx="{size*.24}" fill="{pal[(r*cols+c)%6]}"/>'
    return o


def quick(x, y, w, h, n):
    gap = w / n
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h*.3}" fill="#fff" fill-opacity=".16" stroke="#fff" stroke-opacity=".55"/>'
    return o + tiles(x + gap / 2 - h * .3, y + h * .2, 1, 1, h * .6, 0) + "".join(tiles(x + gap * (i + .5) - h * .3, y + h * .2, 1, 1, h * .6, 0).replace("#ff8a3d", c) for i, c in enumerate(("#42b66e", "#1685e8", "#f2c230", "#e5574f", "#9a7fe0")[:n - 1], 1))


def screen(x, y, w, h, rx=8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="url(#w)"/>'


def phone_front(keyboard):
    h = 590 if keyboard else 520
    sh = 270 if keyboard else 350
    o = WALL + f'<rect x="84" y="16" width="232" height="{h-32}" rx="38" fill="#fff" stroke="{INK}" stroke-width="3"/>'
    o += f'<rect x="170" y="34" width="60" height="6" rx="3" fill="{INK}"/><circle cx="262" cy="37" r="5" fill="{INK}"/>'
    o += screen(102, 56, 196, sh) + tiles(124, 86, 3, 4 if keyboard else 5, 42, 13)
    ga = 56 + sh + 10
    o += f'<rect x="102" y="{ga}" width="196" height="46" rx="16" fill="{WASH}" stroke="{RULE}"/>'
    o += f'<rect x="74" y="150" width="10" height="56" rx="3" fill="{INK}"/><rect x="316" y="{ga-60}" width="10" height="30" rx="3" fill="{INK}"/>'
    o += pin(1, 28, 37, 170, 37) + pin(2, 28, 178, 76, 178) + pin(3, 28, ga + 23, 104, ga + 23)
    n = 4
    if keyboard:
        k = ga + 60
        for r, (off, cnt) in enumerate(((104, 10), (112, 10), (120, 9))):
            for c in range(cnt):
                o += f'<rect x="{off+c*19}" y="{k+r*25}" width="16" height="21" rx="5" fill="{WASH}" stroke="{RULE}"/>'
        o += f'<rect x="104" y="{k+75}" width="24" height="17" rx="5" fill="{WASH}" stroke="{RULE}"/><rect x="160" y="{k+75}" width="80" height="17" rx="5" fill="{WASH}" stroke="{RULE}"/><rect x="272" y="{k+75}" width="24" height="17" rx="5" fill="{WASH}" stroke="{RULE}"/>'
        o += pin(4, 28, k + 38, 112, k + 38)
        n = 5
    o += pin(n, 372, 37, 262, 37) + pin(n + 1, 372, 150, 290, 150) + pin(n + 2, 372, ga - 45, 326, ga - 45)
    o += f'<rect x="185" y="{h-26}" width="30" height="4" rx="2" fill="{INK}"/>' + pin(n + 3, 372, h - 24, 215, h - 24)
    return svg(400, h, o), ("Phone with a keyboard, front view" if keyboard else "Slab phone, front view")


def tablet_frame():
    return WALL + f'<rect x="60" y="16" width="340" height="430" rx="32" fill="#fff" stroke="{INK}" stroke-width="3"/>' + screen(84, 52, 292, 350, 6)


def tablet_figure(kind):
    o = tablet_frame()
    if kind == "front":
        o += tiles(120, 96, 4, 3, 40, 22) + quick(102, 352, 256, 40, 5)
        o += f'<circle cx="230" cy="34" r="4.500" fill="{INK}"/><rect x="208" y="415" width="44" height="14" rx="7" fill="none" stroke="{INK}" stroke-width="2.500"/>'
        o += f'<rect x="56" y="110" width="6" height="210" rx="3" fill="{RULE}"/><rect x="398" y="52" width="8" height="48" rx="3" fill="{INK}"/><rect x="215" y="444" width="30" height="5" rx="2" fill="{INK}"/>'
        o += pin(1, 24, 215, 58, 215) + pin(2, 445, 34, 235, 34) + pin(3, 445, 76, 406, 76) + pin(4, 445, 200, 340, 200) + pin(5, 445, 422, 252, 422) + pin(6, 445, 462, 230, 447, (230, 462))
        return svg(470, 480, o), "Tablet, front view"
    if kind == "card":
        o += '<rect x="130" y="66" width="200" height="22" rx="11" fill="#fff" fill-opacity=".2"/>' + quick(102, 352, 256, 40, 6)
        o += pin(1, 445, 110, 240, 80, (240, 110)) + pin(2, 445, 220, 330, 220) + pin(3, 445, 372, 358, 372)
        return svg(470, 460, o), "Card view on a tablet"
    o += '<rect x="84" y="52" width="292" height="16" fill="#000" fill-opacity=".45"/><rect x="84" y="68" width="292" height="26" fill="#fff" fill-opacity=".14"/>'
    o += tiles(120, 116, 4, 3, 40, 22) + quick(102, 352, 256, 40, 6)
    o += pin(1, 24, 60, 88, 60) + pin(2, 445, 110, 170, 82, (170, 110)) + pin(3, 24, 215, 88, 215) + pin(4, 24, 372, 102, 372)
    o += pin(5, 445, 60, 360, 60) + pin(6, 445, 150, 280, 60, (280, 150))
    return svg(470, 460, o), "Launcher on a tablet"


def phone_screen_figure(kind):
    o = WALL + screen(70, 14, 240, 320, 10)
    if kind == "card":
        o += '<rect x="84" y="30" width="212" height="22" rx="11" fill="#fff" fill-opacity=".2"/>' + quick(82, 272, 216, 48, 5)
        o += pin(1, 350, 80, 190, 41, (190, 80)) + pin(2, 350, 170, 280, 170) + pin(3, 350, 296, 298, 296)
        return svg(370, 348, o), "Card view on a phone"
    o += '<rect x="70" y="14" width="240" height="16" fill="#000" fill-opacity=".5"/><rect x="82" y="38" width="216" height="22" rx="8" fill="#fff" fill-opacity=".16"/>'
    o += tiles(98, 72, 3, 3, 44, 18) + quick(82, 258, 216, 40, 5)
    o += '<rect x="150" y="312" width="150" height="14" rx="7" fill="#fff" fill-opacity=".3"/>'
    o += pin(1, 28, 22, 80, 22) + pin(2, 352, 49, 290, 49) + pin(3, 28, 150, 98, 150) + pin(4, 28, 278, 82, 278)
    o += pin(5, 352, 22, 280, 22) + pin(6, 352, 319, 300, 319)
    return svg(380, 348, o), "Launcher on a phone"


def back_figure():
    o = f'<rect x="60" y="14" width="210" height="350" rx="44" fill="#fff" stroke="{INK}" stroke-width="3"/>'
    o += f'<rect x="88" y="44" width="62" height="56" rx="10" fill="none" stroke="{INK}" stroke-width="2.500"/><circle cx="112" cy="72" r="15" fill="none" stroke="{INK}" stroke-width="3"/><circle cx="112" cy="72" r="6" fill="{INK}"/><circle cx="138" cy="60" r="4.500" fill="{BLUE}"/>'
    o += f'<rect x="130" y="326" width="70" height="12" rx="6" fill="none" stroke="{INK}" stroke-width="2.500"/><rect x="204" y="50" width="14" height="4" rx="2" fill="{INK}"/>'
    o += pin(1, 24, 72, 88, 72) + pin(2, 24, 332, 130, 332) + pin(3, 305, 52, 218, 52)
    return svg(330, 378, o), "Back of the phone"


def top_figure(tablet):
    if tablet:
        o = f'<rect x="60" y="30" width="350" height="26" rx="12" fill="#fff" stroke="{INK}" stroke-width="3"/><circle cx="96" cy="43" r="5" fill="none" stroke="{INK}" stroke-width="2.500"/><rect x="346" y="39" width="30" height="8" rx="4" fill="{INK}"/><circle cx="226" cy="47" r="2" fill="{INK}"/>'
        o += pin(1, 24, 43, 91, 43) + pin(2, 446, 43, 376, 43) + pin(3, 446, 84, 226, 49, (226, 84))
        return svg(470, 104, o), "Top edge of the tablet"
    o = f'<rect x="70" y="24" width="290" height="58" rx="24" fill="#fff" stroke="{INK}" stroke-width="3"/><circle cx="130" cy="52" r="10" fill="none" stroke="{INK}" stroke-width="3"/><rect x="240" y="44" width="32" height="15" rx="7" fill="none" stroke="{INK}" stroke-width="2.500"/><rect x="300" y="44" width="32" height="15" rx="7" fill="{INK}"/>'
    o += pin(1, 24, 52, 120, 52) + pin(2, 402, 52, 332, 52) + pin(3, 402, 98, 256, 59, (256, 98))
    return svg(426, 116, o), "Top edge of the phone"


def key(x, y, w, h, t, fill, ink, size=11):
    lab = f'<text x="{x+w/2}" y="{y+h/2+size*.36}" text-anchor="middle" font-size="{size}" fill="{ink}">{t}</text>' if t else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" stroke="{RULE}"/>' + lab


def keyboard_figure():
    o = f'<rect x="60" y="8" width="300" height="172" rx="26" fill="#fff" stroke="{INK}" stroke-width="3"/>'
    for r, row in enumerate(("qwertyuiop", "asdfghjkl", "zxcvbnm")):
        for c, ch in enumerate(row):
            o += key(82 + r * 8 + c * 25.500, 24 + r * 30, 23, 26, ch.upper(), WASH, INK)
    o += key(72, 114, 30, 26, "", WASH, INK) + key(106, 114, 28, 26, "", WASH, INK) + key(140, 114, 96, 26, "", WASH, INK) + key(308, 114, 34, 26, "Sym", WASH, INK, 10)
    o += key(322, 54, 28, 26, "", WASH, INK) + key(298, 84, 44, 26, "", WASH, INK)
    o += pin(1, 24, 84, 86, 100) + pin(2, 24, 127, 120, 127) + pin(3, 24, 166, 188, 140, (188, 166))
    o += pin(4, 396, 54, 350, 66) + pin(5, 396, 97, 342, 97) + pin(6, 396, 150, 325, 140, (325, 150))
    return svg(420, 188, o), "Physical QWERTY keyboard"


def onscreen_figure():
    o = '<rect x="56" y="8" width="340" height="160" rx="8" fill="#22344f"/>'
    d, t = "#3d506d", "#fff"
    for r, (off, row) in enumerate(((64, "qwertyuiop"), (76, "asdfghjkl"), (100, "zxcvbnm"))):
        for c, ch in enumerate(row):
            o += key(off + c * 28, 16 + r * 37, 25, 32, ch, d, t, 12)
    o += key(64, 127, 40, 32, "Tab", d, t, 11) + key(110, 127, 40, 32, "+=[]", d, t, 10) + key(156, 127, 120, 32, "", d, t) + key(282, 127, 44, 32, "", d, t)
    o += key(332, 127, 54, 32, "", d, t) + key(330, 53, 56, 32, "Enter", d, t, 11)
    o += pin(1, 24, 143, 64, 143) + pin(2, 24, 186, 130, 159, (130, 186)) + pin(3, 428, 69, 386, 69) + pin(4, 428, 143, 386, 143) + pin(5, 428, 186, 216, 159, (216, 186))
    return svg(452, 202, o), "Onscreen keyboard"


def figure(n, slab=False):
    tablet = bool(re.search(r"towi|to3g|topaz", n))
    if "front_view" in n:
        return tablet_figure("front") if tablet else phone_front(not slab)
    if "back_view" in n:
        return back_figure()
    if "top_view" in n:
        return top_figure(tablet)
    if "card_view" in n:
        return tablet_figure("card") if tablet else phone_screen_figure("card")
    if "launcher" in n:
        return tablet_figure("launcher") if tablet else phone_screen_figure("launcher")
    if "keyboard_us" in n:
        return onscreen_figure()
    if "keyboard" in n:
        return keyboard_figure()
    return None


def drawing(name, slab=False):
    n = name.lower()
    fig = figure(n, slab)
    if fig:
        return fig
    if "usb" in n:
        return svg(340, 260, WALL + body_phone(30, 10, 130, 240) + f'<rect x="166" y="150" width="20" height="16" rx="3" fill="{INK}"/><path d="M186 158h120" stroke="{INK}" stroke-width="5"/><path d="M240 130l-24 14 24 14" fill="none" stroke="{BLUE}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'), "Plug the USB cable into the device"
    if "sim" in n:
        return svg(340, 220, f'<rect x="20" y="40" width="210" height="140" rx="16" fill="#fff" stroke="{INK}" stroke-width="3"/><path d="M240 110h50l20 18v40h-70z" fill="{WASH}" stroke="{INK}" stroke-width="2.500"/><rect x="255" y="130" width="34" height="26" rx="3" fill="#e0a800"/><path d="M226 110h-24" stroke="{BLUE}" stroke-width="3"/>'), "Slide the SIM card into its slot"
    if "conceptual" in n:
        def c(x, y, col):
            return f'<rect x="{x}" y="{y}" width="56" height="44" rx="8" fill="{col}"/><circle cx="{x+18}" cy="{y+18}" r="7" fill="#fff"/><rect x="{x+30}" y="{y+13}" width="18" height="5" rx="2.500" fill="#fff"/><rect x="{x+30}" y="{y+24}" width="18" height="5" rx="2.500" fill="#fff"/>'
        arrow = f'<path d="M100 66v36H50M100 66v36h50M100 102v22M92 116l8 10 8-10" fill="none" stroke="{BLUE}" stroke-width="2.500" stroke-linecap="round" stroke-linejoin="round"/>'
        merged = "merged" in n
        return svg(200, 200, c(20, 16, "#1685e8") + c(124, 16, "#42a56b") + arrow + c(72, 140, INK if merged else "#5b6b85")), ("Two contacts merged into one" if merged else "Two contacts linked into one")
    return None
