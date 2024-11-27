'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class User extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  User.init({
    firstname: {
      type: DataTypes.STRING,
      allowNull: true,
    },
    lastname: {
      type: DataTypes.STRING,
      allowNull: true,
    },
    username: DataTypes.STRING,
    email: DataTypes.STRING,
    emailVerified: DataTypes.BOOLEAN,
    verificationToken: DataTypes.STRING,
    verificationExpiry: DataTypes.DATE,
    hash: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'User',
  });
  return User;
};