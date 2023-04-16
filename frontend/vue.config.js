const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

module.exports = {
  devServer: {
    proxy: {
      '/function': {
        target: 'http://212.101.137.104:8080'
      }  
    }
  }
}
