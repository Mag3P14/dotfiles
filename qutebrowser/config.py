config.load_autoconfig(False) 
#config.set("colors.webpage.darkmode.enabled", False)
#c.fonts.default_size = "11pt"
c.url.start_pages = ["https://www.google.com"] # there can be more than one page in the list
c.auto_save.session = True
c.content.autoplay = False
c.tabs.show = "always"
c.tabs.favicons.show = "never"
c.tabs.indicator.width = 2
c.colors.tabs.odd.bg = '#5f5f5f'
c.colors.tabs.even.bg = '#5f5f5f'

config.bind('<g>','scroll-to-perc 0')
config.bind('<Shift+g>','scroll-to-perc 100')
config.bind('<Ctrl-Shift-p>', 'open -p')
config.bind('<Ctrl-Shift-b>', 'history')
config.bind('<o>', 'set-cmd-text -s :open')
config.bind('<Shift+o>', 'set-cmd-text -s :open -t')
config.bind('<Shift+k>', 'tab-next')
config.bind('<Shift+j>', 'tab-prev')
config.bind('<Ctrl-c>','mode-enter passthrough')
config.bind('<Ctrl-s>','open -t https://www.instagram.com/direct/t/101212311274465/#')
config.bind('<Ctrl-q>','set-cmd-text -s :quickmark-add {url} ')
config.bind('ct','tab-clone')
config.bind('qa','quickmark-add')
config.bind('qd','quickmark-del')
config.bind('ql','quickmark-load')
config.bind('<Ctrl-Shift-i>', "edit-text", "insert")
config.bind('g', 'set-cmd-text -s :tab-focus')
#config.bind('<f>', 'hint all tab')
#config.bind('<Shift+f>', 'hint')
c.url.searchengines = {
    "DEFAULT": "https://www.google.com/search?q={}",
}
