// enhanceApp.js
// これだとbuild時にエラーになります
import Vuetify from 'vuetify'
// import 'vuetify.min.css'
// import Vuetify from '../../vuetify'
import '../../../node_modules/vuetify/dist/vuetify.min.css'
import '@mdi/font/css/materialdesignicons.css'
import VueSocialSharing from 'vue-social-sharing'


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
}