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
        ['meta', { name: "og:image", content: "/terada-uspycon2019.jpg" }]
    ],
    themeConfig: {
        logo: '/favicon.jpg',
        nav: [
            { text: 'Home', link: '/' },
            { text: 'About', link: '/about/' },
            { text: 'Episodes', link: '/episodes/' },
            { text: 'Special', link: '/special/' }
        ],
        sidebar: [
            {
                title: 'EPISODES',
                children: [
                    '/episodes/'
                ]
            }
        ],
        searchPlaceholder: 'Search...',
        smoothScroll: true
    },
    plugins: [
        ['@vuepress/google-analytics',
            { 'ga': 'UA-165426465-1' }
        ],
        'aplayer'
    ]
}

