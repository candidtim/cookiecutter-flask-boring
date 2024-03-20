const path = require('path');
const { WebpackManifestPlugin } = require('webpack-manifest-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const RemoveEmptyScriptsPlugin = require('webpack-remove-empty-scripts');

module.exports = {
  entry: {
    main: './src/index.js',
    styles: '/src/styles.scss'
  },
  output: {
    filename: '[name].[contenthash].js',
    publicPath: '/static/',
    path: path.resolve(__dirname, '..','{{cookiecutter.package_name}}', 'static'),
    clean: true
  },
  module: {
    rules: [{
      test: /\.scss$/,
      use: [
        MiniCssExtractPlugin.loader,
        {
          loader: 'css-loader'
        },
        {
          loader: 'sass-loader',
          options: {
            sourceMap: true,
          }
        }
      ]
    }]
  },
  plugins: [
    new WebpackManifestPlugin(),
    new MiniCssExtractPlugin({
      filename: '[name].[contenthash].css'
    }),
    new RemoveEmptyScriptsPlugin()
  ]
};
