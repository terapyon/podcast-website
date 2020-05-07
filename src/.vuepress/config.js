module.exports = {
    title: 'terapyon channel podcast',
    description: 'ここは Manabu TERADA が個人で行っている Podcast の Web サイトです。',
    head: [
        ['link', { rel: 'icon', type: 'image/jpg', href: '/favicon.jpg' }],
        ['meta', { name: "keywords", content: "podcast, terapyon, python" }],
        ['meta', { name: "og:site_name", content: "terapyon channel podcast" }],
        // ['meta', { name: "og:title", content: "Top Page" }],
        // ['meta', { name: "og:description", content: "ここは Manabu TERADA が個人で行っている Podcast の Web サイトです。" }],
        ['meta', { name: "og:type", content: "website" }],
        // ['meta', { name: "og:url", content: "http://podcast.terapyn.net" }],
        ['meta', { name: "og:image", content: "/terada-uspycon2019.jpg" }],
        ['link', { rel: 'manifest', href: '/manifest.json' }],
        ['meta', { name: 'theme-color', content: '#0083BE' }],
        ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
        ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black' }],
        ['link', { rel: 'apple-touch-icon', href: '/icons/icon-152x152.png' }],
        // ['link', { rel: 'mask-icon', href: '/icons/safari-pinned-tab.svg', color: '#3eaf7c' }],
        ['meta', { name: 'msapplication-TileImage', content: '/icons/icon-144x144.png' }],
        ['meta', { name: 'msapplication-TileColor', content: '#000000' }]
    ],
    themeConfig: {
        logo: '/favicon.jpg',
        nav: [
            { text: 'Home', link: '/' },
            { text: 'About', link: '/about/' },
            { text: 'Episodes', link: '/episodes/' },
            { text: 'Special', link: '/special/' }
        ],
        searchPlaceholder: 'Search...',
        smoothScroll: true
    },
    plugins: [
        ['@vuepress/google-analytics',
            { 'ga': 'UA-165426465-1' }
        ],
        'aplayer',
        ['@vuepress/pwa',
            {
                serviceWorker: true,
                updatePopup: false
            }
        ]
    ]
}

