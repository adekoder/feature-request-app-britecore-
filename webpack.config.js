const path = require('path');
const CleanWebpackPlugin = require('clean-webpack-plugin');


module.exports = {
    mode: 'development',
    entry: {
        index: './src/js/index.js'
    },
    devtool: 'inline-source-map',
    plugins:[
        new CleanWebpackPlugin(['app/main/static'])
    ],
    module: {
        rules: [
            {
                test: /\.css$/,
                use:[
                    'style-loader', 'css-loader'
                ]
            }
        ]
    },
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'app/main/static/js')
    }
}