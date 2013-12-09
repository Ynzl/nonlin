#ifndef __INPUT_H__INCLUDED__
#define __INPUT_H__INCLUDED__

#include <cstdlib>          // getenv
#include <sstream>          // istringstream
#include <stdexcept>        // runtime_error
#include <typeinfo>         // typeid

namespace io
{
    template <class T>
    std::string qualify(const std::string& name)
    {
        return typeid(T).name() + (' ' + name);
    }

    // io exceptions
    struct invalid_parameter
        : public std::runtime_error
    {
        invalid_parameter(const std::string& name, const std::string& value)
            : std::runtime_error((name + '=' + value).c_str())
        {
        }
    };

    struct missing_parameter
        : public std::runtime_error
    {
        missing_parameter(const std::string& name)
            : std::runtime_error(name.c_str())
        {
        }
    };

    // get a parameter from the environment
    template <class T>
    T env(const char* name)
    {
        const char* str = std::getenv(name);
        if (!str)
            throw missing_parameter(qualify<T>(name));
        T val;
        std::istringstream in(str);
        if (!(in >> val))
            throw invalid_parameter(qualify<T>(name), str);
        return val;
    }

    template <class T>
    T env(const char* name, const T& deflt)
    {
        try {
            return env<T>(name);
        }
        catch (missing_parameter) {
            return deflt;
        }
    }

    // python3 like print function
    template<typename Ostream, typename T>
    Ostream& print(Ostream& o, T v)
    {
        o << v << std::endl;
        return o;
    }

    template<typename Ostream, typename T, typename... Args>
    Ostream& print(Ostream& o, T v, Args... args)
    {
        o << v << ' ';
        return print(o, args...);
    }

} // ns io

#endif // include guard

