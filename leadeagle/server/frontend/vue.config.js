module.exports = {
    baseUrl: "/frontend",
    devServer: {
        proxy: {
            '/static': {
                target: 'http://localhost:5000',
                ws: true,
                changeOrigin: true
            },
        }
    }
}
