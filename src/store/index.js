// store/index.js

import { createStore } from 'vuex';

export const store = createStore({
    state: {
        featureToggles: [], // Array to store feature toggles
    },
    mutations: {
        addFeatureToggle(state, feature) {
            state.featureToggles.push(feature);
        },
        clearFeatureToggles(state) {
            state.featureToggles = [];
        },
    },
    actions: {
        // eslint-disable-next-line no-unused-vars
        saveFeature({ commit, state }, feature) {
            // Assuming you have an API call to save the feature
            // Here, you would typically make an API call to save the feature
            // For demonstration purposes, we'll just log the feature information
            console.log("feature,,,,", feature)
            console.log('Feature Name:', feature.featureName);
            console.log('Dev Enabled:', feature.devEnabled);
            console.log('Prod Enabled:', feature.prodEnabled);
            console.log('Date Created:', new Date());
            const currentDate = new Date();
            const datePart = currentDate.toLocaleDateString('en-US');
            const timePart = currentDate.toLocaleTimeString('en-US');
            const dateTime = `${datePart} ${timePart}`;
            // Add the feature to the store
            feature.dateCreated = dateTime;
            commit('addFeatureToggle', feature);
        },
    },
    getters: {
        featureToggles: state => state.featureToggles,
    }
});
