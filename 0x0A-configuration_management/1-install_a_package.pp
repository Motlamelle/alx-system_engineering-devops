# puppet script to install flask from pip3: installing package.
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
