// enhanceApp.js
// これだとbuild時にエラーになります
import Vuetify from 'vuetify'
// import 'vuetify.min.css'
// import Vuetify from '../../vuetify'
import '../../../node_modules/vuetify/dist/vuetify.min.css'
import '@mdi/font/css/materialdesignicons.css'
import VueSocialSharing from 'vue-social-sharing'
import { VueReCaptcha } from 'vue-recaptcha-v3'


export default ({
    Vue,
    options,
    router,
    siteData
}) => {
    Vue.use(Vuetify)
    Vue.use(VueSocialSharing)
    options.vuetify = new Vuetify({
        icons: {
            iconfont: 'mdi',
        },
        themes: {
            light: {
                primary: '#41B883'
            },
            dark: {
                primary: '#34495E',
                anchor: '#fff'

            }
        }
    })
    Vue.use([VueReCaptcha, { siteKey: '6Lc3kRwaAAAAAKNIqmQR6yyCIP1Hfnq4wqxMVraJ' }])
}