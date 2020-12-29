const path = require('path')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')

const AppPath = {
  'SRC': path.join('frontend', 'src'),
  'BUILD': path.join('frontend', 'static', 'frontend', 'build')
}

module.exports = {
  context: path.resolve(__dirname, AppPath.SRC),
  entry: {
    app: path.resolve(__dirname, AppPath.SRC, 'index.js')
  },
  output: {
    path: path.resolve(__dirname, AppPath.BUILD),
    filename: '[name].js'
  },
  plugins: [new CleanWebpackPlugin],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ]
  }
}
