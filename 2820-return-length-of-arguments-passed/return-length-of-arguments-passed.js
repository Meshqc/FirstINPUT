/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    const arglen = args.length
    return arglen
};
    
/**
 * argumentsLength(1, 2, 3); // 3
 */