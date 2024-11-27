const usePagination = (resources) => (req, res, next) => {
    const pagination = {};

    const getPaginationParams = (resource = '') => {
        const pageQuery = resource ? `${resource}-page` : 'page';
        const limitQuery = resource ? `${resource}-limit` : 'limit';

        // Parse `page` and `limit` from query params
        const page = parseInt(req.query[pageQuery], 10) || 1; // Default to page 1
        const limit = parseInt(req.query[limitQuery], 10) || 50; // Default to 50 items per page

        // Ensure valid ranges
        if (page < 1) throw new Error('Page must be greater than or equal to 1');
        if (limit < 1 || limit > 100) throw new Error('Limit must be between 1 and 100');

        // Calculate limit and offset
        const offset = (page - 1) * limit;

        return { limit, offset };
    };

    if (resources) {
        // Multi-resource pagination
        resources.forEach(resource => {
            const { limit, offset } = getPaginationParams(resource);
            pagination[resource] = { limit, offset };
        });
        req.pagination = pagination;
        return next();
    };
    
    // Single resource pagination
    const { limit, offset } = getPaginationParams();
    req.pagination = { limit, offset };

    next();

};

module.exports = usePagination;
