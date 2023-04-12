--- 
# Micropython Ref. `ESP32 DOIT`
--- 
<head>
  <style type="text/css">
    th {
        display: none;
    }
    h1 {
        background: #B8B8B8;
    }
    h2 {
        background: #F0F0F0;
    }
    h3 {
        background: #F0F0F0;
    }
  </style>
</head>
Generated: 12.04.2023 16:36:05


## Legende: Links and Buttons
|     |     |
| --- | --- |
| [ein Link](#Overview) | Gleicher Tab. Link innerhalb dieses Dokumentes | |
| <form ><button ><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> | Neuer Tab. Die offizielle Micropython Referenz des entsprechenden Modules wird geöffnet
| <form ><button ><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button></form> | Neuer Tab. Die offizielle Micropython Referenz wird geöffnet und das entsprechende Module highlighted
| <form ><button ><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button></form> | Neuer Tab. Die ESP32 Micropython Referenz wird geöffnet und das entsprechende Module highlighted
| <form ><button ><mark style="background: SkyBlue;"><b>Extern</b></mark></button></form> | Neuer Tab. Intersessante Seite in Bezug zum entsprechenden Micropython Modul wird geöffnet
| <form ><button ><mark style="background: Yellow;"><b>Extern highlight</b></mark></button></form> | Neuer Tab. Intersessante Seite wird geöffnet und das entsprechende Module highlighted
| <form ><button ><mark style="background: Red;"><b>YouTube</b></mark></button></form> | Neuer Tab. YouTube Clip, welche das Thema behandelt
## Overview of all modules <span id="Overview"><span>
| |  |  |  |  |  | 
| --- | --- | --- | --- | --- | --- |
|  [_boot](#_boot) |  [esp](#esp) |  [onewire](#onewire) |  [uctypes](#uctypes) |  [upip_utarfile](#upip_utarfile) |  [utime](#utime) |
|  [_onewire](#_onewire) |  [esp32](#esp32) |  [uarray](#uarray) |  [uerrno](#uerrno) |  [uplatform](#uplatform) |  [utimeq](#utimeq) |
|  [_thread](#_thread) |  [flashbdev](#flashbdev) |  [uasyncio/core](#uasyncio/core) |  [uhashlib](#uhashlib) |  [upysh](#upysh) |  [uwebsocket](#uwebsocket) |
|  [_uasyncio](#_uasyncio) |  [framebuf](#framebuf) |  [uasyncio/event](#uasyncio/event) |  [uheapq](#uheapq) |  [urandom](#urandom) |  [uzlib](#uzlib) |
|  [_webrepl](#_webrepl) |  [gc](#gc) |  [uasyncio/funcs](#uasyncio/funcs) |  [uio](#uio) |  [ure](#ure) |  [webrepl](#webrepl) |
|  [apa106](#apa106) |  [inisetup](#inisetup) |  [uasyncio/lock](#uasyncio/lock) |  [ujson](#ujson) |  [urequests](#urequests) |  [webrepl_setup](#webrepl_setup) |
|  [btree](#btree) |  [math](#math) |  [uasyncio/stream](#uasyncio/stream) |  [umachine](#umachine) |  [uselect](#uselect) |  [websocket_helper](#websocket_helper) |
|  [builtins](#builtins) |  [micropython](#micropython) |  [ubinascii](#ubinascii) |  [umqtt/robust](#umqtt/robust) |  [usocket](#usocket) | |
|  [cmath](#cmath) |  [neopixel](#neopixel) |  [ubluetooth](#ubluetooth) |  [umqtt/simple](#umqtt/simple) |  [ussl](#ussl) | |
|  [dht](#dht) |  [network](#network) |  [ucollections](#ucollections) |  [uos](#uos) |  [ustruct](#ustruct) | |
|  [ds18x20](#ds18x20) |  [ntptime](#ntptime) |  [ucryptolib](#ucryptolib) |  [upip](#upip) |  [usys](#usys) | |
# _boot <span id="_boot"></span>

  * `object <module '_boot' from '_boot.py'> is of type module`
  * `uos -- <module 'uos'>`
  * `__name__ -- _boot`
  * `gc -- <module 'gc'>`
  * `__file__ -- _boot.py`
  * `bdev -- <Partition type=1, subtype=129, address=2097152, size=2097152, label=vfs, encrypted=0>`

[--> Overview](#Overview)
# _onewire <span id="_onewire"></span>

  * `object <module 'onewire'> is of type module`
  * `__name__ -- onewire`
  * `reset -- <function>`
  * `readbit -- <function>`
  * `readbyte -- <function>`
  * `writebit -- <function>`
  * `writebyte -- <function>`
  * `crc8 -- <function>`

[--> Overview](#Overview)
# _thread <span id="_thread"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/_thread.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module '_thread'> is of type module`
  * `__name__ -- _thread`
  * [`LockType -- <class 'lock'>`](#_thread.LockType)
  * `get_ident -- <function>`
  * `stack_size -- <function>`
  * `start_new_thread -- <function>`
  * `exit -- <function>`
  * `allocate_lock -- <function>`

[--> Overview](#Overview)
## _thread --> LockType <span id="_thread.LockType"></span>

  * `__enter__ -- <function>`
  * `__exit__ -- <function>`
  * `acquire -- <function>`
  * `locked -- <function>`
  * `object <class 'lock'> is of type type`
  * `release -- <function>`

[--> _thread](#_thread)

[--> Overview](#Overview)
# _uasyncio <span id="_uasyncio"></span>

  * `object <module '_uasyncio'> is of type module`
  * `__name__ -- _uasyncio`
  * [`TaskQueue -- <class 'TaskQueue'>`](#_uasyncio.TaskQueue)
  * [`Task -- <class 'Task'>`](#_uasyncio.Task)

[--> Overview](#Overview)
## _uasyncio --> TaskQueue <span id="_uasyncio.TaskQueue"></span>

  * `object <class 'TaskQueue'> is of type type`
  * `peek -- <function>`
  * `pop -- <function>`
  * `push -- <function>`
  * `remove -- <function>`

[--> _uasyncio](#_uasyncio)

[--> Overview](#Overview)
## _uasyncio --> Task <span id="_uasyncio.Task"></span>

  * `object <class 'Task'> is of type type`

[--> _uasyncio](#_uasyncio)

[--> Overview](#Overview)
# _webrepl <span id="_webrepl"></span>

  * `object <module '_webrepl'> is of type module`
  * `__name__ -- _webrepl`
  * [`_webrepl -- <class '_webrepl'>`](#_webrepl._webrepl)
  * `password -- <function>`

[--> Overview](#Overview)
## _webrepl --> _webrepl <span id="_webrepl._webrepl"></span>

  * `close -- <function>`
  * `object <class '_webrepl'> is of type type`
  * `read -- <function>`
  * `readinto -- <function>`
  * `write -- <function>`

[--> _webrepl](#_webrepl)

[--> Overview](#Overview)
# apa106 <span id="apa106"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/esp32/quickref.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button><input  type="hidden" name="highlight" value="apa106" /> </form> |

  * `object <module 'apa106' from 'apa106.py'> is of type module`
  * [`APA106 -- <class 'APA106'>`](#apa106.APA106)
  * [`NeoPixel -- <class 'NeoPixel'>`](#apa106.NeoPixel)
  * `__name__ -- apa106`
  * `__file__ -- apa106.py`

[--> Overview](#Overview)
## apa106 --> APA106 <span id="apa106.APA106"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/esp32/quickref.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button><input  type="hidden" name="highlight" value="APA106" /> </form> |

  * `ORDER -- (0, 1, 2, 3)`
  * `__module__ -- apa106`
  * `__qualname__ -- APA106`
  * `object <class 'APA106'> is of type type`

[--> apa106](#apa106)

[--> Overview](#Overview)
## apa106 --> NeoPixel <span id="apa106.NeoPixel"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/esp32/quickref.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button><input  type="hidden" name="highlight" value="NeoPixel" /> </form> |

  * `ORDER -- (1, 0, 2, 3)`
  * `__getitem__ -- <function __getitem__ at 0x3ffe8e10>`
  * `__init__ -- <function __init__ at 0x3ffe8e20>`
  * `__len__ -- <function __len__ at 0x3ffe8e40>`
  * `__module__ -- neopixel`
  * `__qualname__ -- NeoPixel`
  * `__setitem__ -- <function __setitem__ at 0x3ffe8e00>`
  * `fill -- <function fill at 0x3ffe8e50>`
  * `object <class 'NeoPixel'> is of type type`
  * `write -- <function write at 0x3ffe8e60>`

[--> apa106](#apa106)

[--> Overview](#Overview)
# btree <span id="btree"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/btree.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'btree'> is of type module`
  * `__name__ -- btree`
  * `open -- <function>`
  * `INCL -- 1`
  * `DESC -- 2`

[--> Overview](#Overview)
# builtins <span id="builtins"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'builtins'> is of type module`
  * `__name__ -- builtins`
  * `__build_class__ -- <function>`
  * `__import__ -- <function>`
  * `__repl_print__ -- <function>`
  * [`bool -- <class 'bool'>`](#builtins.bool)
  * [`bytes -- <class 'bytes'>`](#builtins.bytes)
  * [`bytearray -- <class 'bytearray'>`](#builtins.bytearray)
  * [`complex -- <class 'complex'>`](#builtins.complex)
  * [`dict -- <class 'dict'>`](#builtins.dict)
  * [`enumerate -- <class 'enumerate'>`](#builtins.enumerate)
  * [`filter -- <class 'filter'>`](#builtins.filter)
  * [`float -- <class 'float'>`](#builtins.float)
  * [`frozenset -- <class 'frozenset'>`](#builtins.frozenset)
  * [`int -- <class 'int'>`](#builtins.int)
  * [`list -- <class 'list'>`](#builtins.list)
  * [`map -- <class 'map'>`](#builtins.map)
  * [`memoryview -- <class 'memoryview'>`](#builtins.memoryview)
  * [`object -- <class 'object'>`](#builtins.object)
  * [`property -- <class 'property'>`](#builtins.property)
  * [`range -- <class 'range'>`](#builtins.range)
  * [`reversed -- <class 'reversed'>`](#builtins.reversed)
  * [`set -- <class 'set'>`](#builtins.set)
  * [`slice -- <class 'slice'>`](#builtins.slice)
  * [`str -- <class 'str'>`](#builtins.str)
  * [`super -- <class 'super'>`](#builtins.super)
  * [`tuple -- <class 'tuple'>`](#builtins.tuple)
  * [`type -- <class 'type'>`](#builtins.type)
  * [`zip -- <class 'zip'>`](#builtins.zip)
  * [`classmethod -- <class 'classmethod'>`](#builtins.classmethod)
  * [`staticmethod -- <class 'staticmethod'>`](#builtins.staticmethod)
  * `Ellipsis -- Ellipsis`
  * `NotImplemented -- NotImplemented`
  * `abs -- <function>`
  * `all -- <function>`
  * `any -- <function>`
  * `bin -- <function>`
  * `callable -- <function>`
  * `compile -- <function>`
  * `chr -- <function>`
  * `delattr -- <function>`
  * `dir -- <function>`
  * `divmod -- <function>`
  * `eval -- <function>`
  * `exec -- <function>`
  * `execfile -- <function>`
  * `getattr -- <function>`
  * `setattr -- <function>`
  * `globals -- <function>`
  * `hasattr -- <function>`
  * `hash -- <function>`
  * `help -- <function>`
  * `hex -- <function>`
  * `id -- <function>`
  * `input -- <function>`
  * `isinstance -- <function>`
  * `issubclass -- <function>`
  * `iter -- <function>`
  * `len -- <function>`
  * `locals -- <function>`
  * `max -- <function>`
  * `min -- <function>`
  * `next -- <function>`
  * `oct -- <function>`
  * `open -- <function>`
  * `ord -- <function>`
  * `pow -- <function>`
  * `print -- <function>`
  * `repr -- <function>`
  * `round -- <function>`
  * `sorted -- <function>`
  * `sum -- <function>`
  * [`BaseException -- <class 'BaseException'>`](#builtins.BaseException)
  * [`ArithmeticError -- <class 'ArithmeticError'>`](#builtins.ArithmeticError)
  * [`AssertionError -- <class 'AssertionError'>`](#builtins.AssertionError)
  * [`AttributeError -- <class 'AttributeError'>`](#builtins.AttributeError)
  * [`EOFError -- <class 'EOFError'>`](#builtins.EOFError)
  * [`Exception -- <class 'Exception'>`](#builtins.Exception)
  * [`GeneratorExit -- <class 'GeneratorExit'>`](#builtins.GeneratorExit)
  * [`ImportError -- <class 'ImportError'>`](#builtins.ImportError)
  * [`IndentationError -- <class 'IndentationError'>`](#builtins.IndentationError)
  * [`IndexError -- <class 'IndexError'>`](#builtins.IndexError)
  * [`KeyboardInterrupt -- <class 'KeyboardInterrupt'>`](#builtins.KeyboardInterrupt)
  * [`KeyError -- <class 'KeyError'>`](#builtins.KeyError)
  * [`LookupError -- <class 'LookupError'>`](#builtins.LookupError)
  * [`MemoryError -- <class 'MemoryError'>`](#builtins.MemoryError)
  * [`NameError -- <class 'NameError'>`](#builtins.NameError)
  * [`NotImplementedError -- <class 'NotImplementedError'>`](#builtins.NotImplementedError)
  * [`OSError -- <class 'OSError'>`](#builtins.OSError)
  * [`OverflowError -- <class 'OverflowError'>`](#builtins.OverflowError)
  * [`RuntimeError -- <class 'RuntimeError'>`](#builtins.RuntimeError)
  * [`StopAsyncIteration -- <class 'StopAsyncIteration'>`](#builtins.StopAsyncIteration)
  * [`StopIteration -- <class 'StopIteration'>`](#builtins.StopIteration)
  * [`SyntaxError -- <class 'SyntaxError'>`](#builtins.SyntaxError)
  * [`SystemExit -- <class 'SystemExit'>`](#builtins.SystemExit)
  * [`TypeError -- <class 'TypeError'>`](#builtins.TypeError)
  * [`UnicodeError -- <class 'UnicodeError'>`](#builtins.UnicodeError)
  * [`ValueError -- <class 'ValueError'>`](#builtins.ValueError)
  * [`ViperTypeError -- <class 'ViperTypeError'>`](#builtins.ViperTypeError)
  * [`ZeroDivisionError -- <class 'ZeroDivisionError'>`](#builtins.ZeroDivisionError)

[--> Overview](#Overview)
## builtins --> bool <span id="builtins.bool"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="bool" /> </form> |

  * `object <class 'bool'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> bytes <span id="builtins.bytes"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="bytes" /> </form> |

  * `center -- <function>`
  * `count -- <function>`
  * `decode -- <function>`
  * `endswith -- <function>`
  * `find -- <function>`
  * `format -- <function>`
  * `index -- <function>`
  * `isalpha -- <function>`
  * `isdigit -- <function>`
  * `islower -- <function>`
  * `isspace -- <function>`
  * `isupper -- <function>`
  * `join -- <function>`
  * `lower -- <function>`
  * `lstrip -- <function>`
  * `object <class 'bytes'> is of type type`
  * `partition -- <function>`
  * `replace -- <function>`
  * `rfind -- <function>`
  * `rindex -- <function>`
  * `rpartition -- <function>`
  * `rsplit -- <function>`
  * `rstrip -- <function>`
  * `split -- <function>`
  * `splitlines -- <function>`
  * `startswith -- <function>`
  * `strip -- <function>`
  * `upper -- <function>`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> bytearray <span id="builtins.bytearray"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="bytearray" /> </form> |

  * `append -- <function>`
  * `decode -- <function>`
  * `extend -- <function>`
  * `object <class 'bytearray'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> complex <span id="builtins.complex"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="complex" /> </form> |

  * `object <class 'complex'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> dict <span id="builtins.dict"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="dict" /> </form> |

  * `__delitem__ -- <function>`
  * `__getitem__ -- <function>`
  * `__setitem__ -- <function>`
  * `clear -- <function>`
  * `copy -- <function>`
  * `fromkeys -- <classmethod>`
  * `get -- <function>`
  * `items -- <function>`
  * `keys -- <function>`
  * `object <class 'dict'> is of type type`
  * `pop -- <function>`
  * `popitem -- <function>`
  * `setdefault -- <function>`
  * `update -- <function>`
  * `values -- <function>`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> enumerate <span id="builtins.enumerate"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="enumerate" /> </form> |

  * `object <class 'enumerate'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> filter <span id="builtins.filter"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="filter" /> </form> |

  * `object <class 'filter'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> float <span id="builtins.float"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="float" /> </form> |

  * `object <class 'float'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> frozenset <span id="builtins.frozenset"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="frozenset" /> </form> |

  * `__contains__ -- <function>`
  * `copy -- <function>`
  * `difference -- <function>`
  * `intersection -- <function>`
  * `isdisjoint -- <function>`
  * `issubset -- <function>`
  * `issuperset -- <function>`
  * `object <class 'frozenset'> is of type type`
  * `symmetric_difference -- <function>`
  * `union -- <function>`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> int <span id="builtins.int"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="int" /> </form> |

  * `from_bytes -- <classmethod>`
  * `object <class 'int'> is of type type`
  * `to_bytes -- <function>`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> list <span id="builtins.list"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="list" /> </form> |

  * `append -- <function>`
  * `clear -- <function>`
  * `copy -- <function>`
  * `count -- <function>`
  * `extend -- <function>`
  * `index -- <function>`
  * `insert -- <function>`
  * `object <class 'list'> is of type type`
  * `pop -- <function>`
  * `remove -- <function>`
  * `reverse -- <function>`
  * `sort -- <function>`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> map <span id="builtins.map"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="map" /> </form> |

  * `object <class 'map'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> memoryview <span id="builtins.memoryview"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="memoryview" /> </form> |

  * `object <class 'memoryview'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> object <span id="builtins.object"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="object" /> </form> |

  * `__delattr__ -- <function>`
  * `__init__ -- <function>`
  * `__new__ -- <staticmethod>`
  * `__setattr__ -- <function>`
  * `object <class 'object'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> property <span id="builtins.property"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="property" /> </form> |

  * `deleter -- <function>`
  * `getter -- <function>`
  * `object <class 'property'> is of type type`
  * `setter -- <function>`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> range <span id="builtins.range"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="range" /> </form> |

  * `object <class 'range'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> reversed <span id="builtins.reversed"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="reversed" /> </form> |

  * `object <class 'reversed'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> set <span id="builtins.set"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="set" /> </form> |

  * `__contains__ -- <function>`
  * `add -- <function>`
  * `clear -- <function>`
  * `copy -- <function>`
  * `difference -- <function>`
  * `difference_update -- <function>`
  * `discard -- <function>`
  * `intersection -- <function>`
  * `intersection_update -- <function>`
  * `isdisjoint -- <function>`
  * `issubset -- <function>`
  * `issuperset -- <function>`
  * `object <class 'set'> is of type type`
  * `pop -- <function>`
  * `remove -- <function>`
  * `symmetric_difference -- <function>`
  * `symmetric_difference_update -- <function>`
  * `union -- <function>`
  * `update -- <function>`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> slice <span id="builtins.slice"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="slice" /> </form> |

  * `object <class 'slice'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> str <span id="builtins.str"></span>

|    |    |
| --- | --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="str" /> </form> | <form action="https://www.w3schools.com/python/python_strings_methods.asp"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>Extern</b></mark></button></form> |

  * `center -- <function>`
  * `count -- <function>`
  * `encode -- <function>`
  * `endswith -- <function>`
  * `find -- <function>`
  * `format -- <function>`
  * `index -- <function>`
  * `isalpha -- <function>`
  * `isdigit -- <function>`
  * `islower -- <function>`
  * `isspace -- <function>`
  * `isupper -- <function>`
  * `join -- <function>`
  * `lower -- <function>`
  * `lstrip -- <function>`
  * `object <class 'str'> is of type type`
  * `partition -- <function>`
  * `replace -- <function>`
  * `rfind -- <function>`
  * `rindex -- <function>`
  * `rpartition -- <function>`
  * `rsplit -- <function>`
  * `rstrip -- <function>`
  * `split -- <function>`
  * `splitlines -- <function>`
  * `startswith -- <function>`
  * `strip -- <function>`
  * `upper -- <function>`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> super <span id="builtins.super"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="super" /> </form> |

  * `object <class 'super'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> tuple <span id="builtins.tuple"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="tuple" /> </form> |

  * `count -- <function>`
  * `index -- <function>`
  * `object <class 'tuple'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> type <span id="builtins.type"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="type" /> </form> |

  * `object <class 'type'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> zip <span id="builtins.zip"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="zip" /> </form> |

  * `object <class 'zip'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> classmethod <span id="builtins.classmethod"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="classmethod" /> </form> |

  * `object <class 'classmethod'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> staticmethod <span id="builtins.staticmethod"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="staticmethod" /> </form> |

  * `object <class 'staticmethod'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> BaseException <span id="builtins.BaseException"></span>

  * `object <class 'BaseException'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> ArithmeticError <span id="builtins.ArithmeticError"></span>

|    |
| --- |
| <form action="https://docs.python.org/3/library/exceptions.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>Extern highlight</b></mark></button><input  type="hidden" name="highlight" value="ArithmeticError" /> </form> |

  * `object <class 'ArithmeticError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> AssertionError <span id="builtins.AssertionError"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="AssertionError" /> </form> |

  * `object <class 'AssertionError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> AttributeError <span id="builtins.AttributeError"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="AttributeError" /> </form> |

  * `object <class 'AttributeError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> EOFError <span id="builtins.EOFError"></span>

|    |
| --- |
| <form action="https://docs.python.org/3/library/exceptions.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>Extern highlight</b></mark></button><input  type="hidden" name="highlight" value="EOFError" /> </form> |

  * `object <class 'EOFError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> Exception <span id="builtins.Exception"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="Exception" /> </form> |

  * `object <class 'Exception'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> GeneratorExit <span id="builtins.GeneratorExit"></span>

  * `object <class 'GeneratorExit'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> ImportError <span id="builtins.ImportError"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="ImportError" /> </form> |

  * `object <class 'ImportError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> IndentationError <span id="builtins.IndentationError"></span>

|    |
| --- |
| <form action="https://docs.python.org/3/library/exceptions.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>Extern highlight</b></mark></button><input  type="hidden" name="highlight" value="IndentationError" /> </form> |

  * `object <class 'IndentationError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> IndexError <span id="builtins.IndexError"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="IndexError" /> </form> |

  * `object <class 'IndexError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> KeyboardInterrupt <span id="builtins.KeyboardInterrupt"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="KeyboardInterrupt" /> </form> |

  * `object <class 'KeyboardInterrupt'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> KeyError <span id="builtins.KeyError"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="KeyError" /> </form> |

  * `object <class 'KeyError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> LookupError <span id="builtins.LookupError"></span>

|    |
| --- |
| <form action="https://docs.python.org/3/library/exceptions.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>Extern highlight</b></mark></button><input  type="hidden" name="highlight" value="LookupError" /> </form> |

  * `object <class 'LookupError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> MemoryError <span id="builtins.MemoryError"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="MemoryError" /> </form> |

  * `object <class 'MemoryError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> NameError <span id="builtins.NameError"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="NameError" /> </form> |

  * `object <class 'NameError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> NotImplementedError <span id="builtins.NotImplementedError"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="NotImplementedError" /> </form> |

  * `object <class 'NotImplementedError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> OSError <span id="builtins.OSError"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="OSError" /> </form> |

  * `object <class 'OSError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> OverflowError <span id="builtins.OverflowError"></span>

|    |
| --- |
| <form action="https://docs.python.org/3/library/exceptions.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>Extern highlight</b></mark></button><input  type="hidden" name="highlight" value="OverflowError" /> </form> |

  * `object <class 'OverflowError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> RuntimeError <span id="builtins.RuntimeError"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="RuntimeError" /> </form> |

  * `object <class 'RuntimeError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> StopAsyncIteration <span id="builtins.StopAsyncIteration"></span>

  * `object <class 'StopAsyncIteration'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> StopIteration <span id="builtins.StopIteration"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="StopIteration" /> </form> |

  * `object <class 'StopIteration'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> SyntaxError <span id="builtins.SyntaxError"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="SyntaxError" /> </form> |

  * `object <class 'SyntaxError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> SystemExit <span id="builtins.SystemExit"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="SystemExit" /> </form> |

  * `object <class 'SystemExit'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> TypeError <span id="builtins.TypeError"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="TypeError" /> </form> |

  * `object <class 'TypeError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> UnicodeError <span id="builtins.UnicodeError"></span>

|    |
| --- |
| <form action="https://docs.python.org/3/library/exceptions.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>Extern highlight</b></mark></button><input  type="hidden" name="highlight" value="UnicodeError" /> </form> |

  * `object <class 'UnicodeError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> ValueError <span id="builtins.ValueError"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="ValueError" /> </form> |

  * `object <class 'ValueError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> ViperTypeError <span id="builtins.ViperTypeError"></span>

  * `object <class 'ViperTypeError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
## builtins --> ZeroDivisionError <span id="builtins.ZeroDivisionError"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/builtins.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="ZeroDivisionError" /> </form> |

  * `object <class 'ZeroDivisionError'> is of type type`

[--> builtins](#builtins)

[--> Overview](#Overview)
# cmath <span id="cmath"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/cmath.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'cmath'> is of type module`
  * `__name__ -- cmath`
  * `e -- 2.718282`
  * `pi -- 3.141593`
  * `phase -- <function>`
  * `polar -- <function>`
  * `rect -- <function>`
  * `exp -- <function>`
  * `log -- <function>`
  * `log10 -- <function>`
  * `sqrt -- <function>`
  * `cos -- <function>`
  * `sin -- <function>`

[--> Overview](#Overview)
# dht <span id="dht"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/esp32/quickref.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button><input  type="hidden" name="highlight" value="dht" /> </form> |

  * `object <module 'dht' from 'dht.py'> is of type module`
  * [`DHTBase -- <class 'DHTBase'>`](#dht.DHTBase)
  * `__name__ -- dht`
  * `__file__ -- dht.py`
  * `sys -- <module 'sys'>`
  * [`DHT11 -- <class 'DHT11'>`](#dht.DHT11)
  * `dht_readinto -- <function>`
  * [`DHT22 -- <class 'DHT22'>`](#dht.DHT22)

[--> Overview](#Overview)
## dht --> DHTBase <span id="dht.DHTBase"></span>

  * `__init__ -- <function __init__ at 0x3fff9e20>`
  * `__module__ -- dht`
  * `__qualname__ -- DHTBase`
  * `measure -- <function measure at 0x3fff9e10>`
  * `object <class 'DHTBase'> is of type type`

[--> dht](#dht)

[--> Overview](#Overview)
## dht --> DHT11 <span id="dht.DHT11"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/esp32/quickref.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button><input  type="hidden" name="highlight" value="DHT11" /> </form> |

  * `__module__ -- dht`
  * `__qualname__ -- DHT11`
  * `humidity -- <function humidity at 0x3fff9ed0>`
  * `object <class 'DHT11'> is of type type`
  * `temperature -- <function temperature at 0x3fff9ec0>`

[--> dht](#dht)

[--> Overview](#Overview)
## dht --> DHT22 <span id="dht.DHT22"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/esp32/quickref.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button><input  type="hidden" name="highlight" value="DHT22" /> </form> |

  * `__module__ -- dht`
  * `__qualname__ -- DHT22`
  * `humidity -- <function humidity at 0x3fff9f80>`
  * `object <class 'DHT22'> is of type type`
  * `temperature -- <function temperature at 0x3fff9f70>`

[--> dht](#dht)

[--> Overview](#Overview)
# ds18x20 <span id="ds18x20"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/esp32/quickref.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button><input  type="hidden" name="highlight" value="ds18x20" /> </form> |

  * `object <module 'ds18x20' from 'ds18x20.py'> is of type module`
  * `const -- <function>`
  * [`DS18X20 -- <class 'DS18X20'>`](#ds18x20.DS18X20)
  * `__name__ -- ds18x20`
  * `__file__ -- ds18x20.py`

[--> Overview](#Overview)
## ds18x20 --> DS18X20 <span id="ds18x20.DS18X20"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/esp32/quickref.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button><input  type="hidden" name="highlight" value="DS18X20" /> </form> |

  * `__init__ -- <function __init__ at 0x3fffb5a0>`
  * `__module__ -- ds18x20`
  * `__qualname__ -- DS18X20`
  * `convert_temp -- <function convert_temp at 0x3fffb5d0>`
  * `object <class 'DS18X20'> is of type type`
  * `read_scratch -- <function read_scratch at 0x3fffb5b0>`
  * `read_temp -- <function read_temp at 0x3fffb5e0>`
  * `scan -- <function scan at 0x3fffb590>`
  * `write_scratch -- <function write_scratch at 0x3fffb5c0>`

[--> ds18x20](#ds18x20)

[--> Overview](#Overview)
# esp <span id="esp"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/esp.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'esp'> is of type module`
  * `__name__ -- esp`
  * `osdebug -- <function>`
  * `flash_read -- <function>`
  * `flash_write -- <function>`
  * `flash_erase -- <function>`
  * `flash_size -- <function>`
  * `flash_user_start -- <function>`
  * `gpio_matrix_in -- <function>`
  * `gpio_matrix_out -- <function>`
  * `dht_readinto -- <function>`
  * `LOG_NONE -- 0`
  * `LOG_ERROR -- 1`
  * `LOG_WARNING -- 2`
  * `LOG_INFO -- 3`
  * `LOG_DEBUG -- 4`
  * `LOG_VERBOSE -- 5`

[--> Overview](#Overview)
# esp32 <span id="esp32"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/esp32.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'esp32'> is of type module`
  * `__name__ -- esp32`
  * `wake_on_touch -- <function>`
  * `wake_on_ext0 -- <function>`
  * `wake_on_ext1 -- <function>`
  * `gpio_deep_sleep_hold -- <function>`
  * `raw_temperature -- <function>`
  * `hall_sensor -- <function>`
  * `idf_heap_info -- <function>`
  * [`NVS -- <class 'NVS'>`](#esp32.NVS)
  * [`Partition -- <class 'Partition'>`](#esp32.Partition)
  * [`RMT -- <class 'RMT'>`](#esp32.RMT)
  * [`ULP -- <class 'ULP'>`](#esp32.ULP)
  * `WAKEUP_ALL_LOW -- False`
  * `WAKEUP_ANY_HIGH -- True`
  * `HEAP_DATA -- 4`
  * `HEAP_EXEC -- 1`

[--> Overview](#Overview)
## esp32 --> NVS <span id="esp32.NVS"></span>

|    |    |    |    |
| --- | --- | --- | --- |
| <form action="https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/storage/nvs_flash.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>Extern</b></mark></button></form> | <form action="https://docs.micropython.org/en/v1.19/library/esp32.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="NVS" /> </form> | <form action="https://insigh.io/blog/over-the-air-switch-from-esp-idf-to-micropython/"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>Extern</b></mark></button></form> | <form action="https://www.youtube.com/watch" method="get" target="_blank"><button type="submit"><mark style="background: Red;"><b>YouTube</b></mark></button><input  type="hidden" name="v" value="CX5-dAmOxRc" /> </form> |

  * `commit -- <function>`
  * `erase_key -- <function>`
  * `get_blob -- <function>`
  * `get_i32 -- <function>`
  * `object <class 'NVS'> is of type type`
  * `set_blob -- <function>`
  * `set_i32 -- <function>`

[--> esp32](#esp32)

[--> Overview](#Overview)
## esp32 --> Partition <span id="esp32.Partition"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/esp32.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="Partition" /> </form> |

  * `BOOT -- 0`
  * `RUNNING -- 1`
  * `TYPE_APP -- 0`
  * `TYPE_DATA -- 1`
  * `find -- <staticmethod>`
  * `get_next_update -- <function>`
  * `info -- <function>`
  * `ioctl -- <function>`
  * `mark_app_valid_cancel_rollback -- <classmethod>`
  * `object <class 'Partition'> is of type type`
  * `readblocks -- <function>`
  * `set_boot -- <function>`
  * `writeblocks -- <function>`

[--> esp32](#esp32)

[--> Overview](#Overview)
## esp32 --> RMT <span id="esp32.RMT"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/esp32/quickref.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button><input  type="hidden" name="highlight" value="RMT" /> </form> |

  * `__del__ -- <function>`
  * `bitstream_channel -- <staticmethod>`
  * `clock_div -- <function>`
  * `deinit -- <function>`
  * `loop -- <function>`
  * `object <class 'RMT'> is of type type`
  * `source_freq -- <function>`
  * `wait_done -- <function>`
  * `write_pulses -- <function>`

[--> esp32](#esp32)

[--> Overview](#Overview)
## esp32 --> ULP <span id="esp32.ULP"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/esp32/quickref.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button><input  type="hidden" name="highlight" value="ULP" /> </form> |

  * `RESERVE_MEM -- 512`
  * `load_binary -- <function>`
  * `object <class 'ULP'> is of type type`
  * `run -- <function>`
  * `set_wakeup_period -- <function>`

[--> esp32](#esp32)

[--> Overview](#Overview)
# flashbdev <span id="flashbdev"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/v1.19/reference/filesystem.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>Extern highlight</b></mark></button><input  type="hidden" name="highlight" value="flashbdev" /> </form> |

  * `object <module 'flashbdev' from 'flashbdev.py'> is of type module`
  * [`Partition -- <class 'Partition'>`](#flashbdev.Partition)
  * `bdev -- <Partition type=1, subtype=129, address=2097152, size=2097152, label=vfs, encrypted=0>`
  * `__name__ -- flashbdev`
  * `__file__ -- flashbdev.py`

[--> Overview](#Overview)
## flashbdev --> Partition <span id="flashbdev.Partition"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/v1.19/reference/filesystem.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>Extern highlight</b></mark></button><input  type="hidden" name="highlight" value="Partition" /> </form> |

  * `BOOT -- 0`
  * `RUNNING -- 1`
  * `TYPE_APP -- 0`
  * `TYPE_DATA -- 1`
  * `find -- <staticmethod>`
  * `get_next_update -- <function>`
  * `info -- <function>`
  * `ioctl -- <function>`
  * `mark_app_valid_cancel_rollback -- <classmethod>`
  * `object <class 'Partition'> is of type type`
  * `readblocks -- <function>`
  * `set_boot -- <function>`
  * `writeblocks -- <function>`

[--> flashbdev](#flashbdev)

[--> Overview](#Overview)
# framebuf <span id="framebuf"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/framebuf.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'framebuf'> is of type module`
  * `__name__ -- framebuf`
  * [`FrameBuffer -- <class 'FrameBuffer'>`](#framebuf.FrameBuffer)
  * `FrameBuffer1 -- <function>`
  * `MVLSB -- 0`
  * `MONO_VLSB -- 0`
  * `RGB565 -- 1`
  * `GS2_HMSB -- 5`
  * `GS4_HMSB -- 2`
  * `GS8 -- 6`
  * `MONO_HLSB -- 3`
  * `MONO_HMSB -- 4`

[--> Overview](#Overview)
## framebuf --> FrameBuffer <span id="framebuf.FrameBuffer"></span>

|    |    |    |
| --- | --- | --- |
| <form action="https://blog.miguelgrinberg.com/post/micropython-and-the-internet-of-things-part-vi-working-with-a-screen"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>Extern</b></mark></button></form> | <form action="https://docs.micropython.org/en/latest/library/framebuf.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> | <form action="https://www.youtube.com/watch" method="get" target="_blank"><button type="submit"><mark style="background: Red;"><b>YouTube</b></mark></button><input  type="hidden" name="v" value="uuFm-mp2S64" /> </form> |

  * `blit -- <function>`
  * `fill -- <function>`
  * `fill_rect -- <function>`
  * `hline -- <function>`
  * `line -- <function>`
  * `object <class 'FrameBuffer'> is of type type`
  * `pixel -- <function>`
  * `rect -- <function>`
  * `scroll -- <function>`
  * `text -- <function>`
  * `vline -- <function>`

[--> framebuf](#framebuf)

[--> Overview](#Overview)
# gc <span id="gc"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/gc.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'gc'> is of type module`
  * `__name__ -- gc`
  * `collect -- <function>`
  * `disable -- <function>`
  * `enable -- <function>`
  * `isenabled -- <function>`
  * `mem_free -- <function>`
  * `mem_alloc -- <function>`
  * `threshold -- <function>`

[--> Overview](#Overview)
# inisetup <span id="inisetup"></span>

|    |
| --- |
| <form action="https://github.com/micropython/micropython-esp32/blob/esp32/ports/esp32/modules/inisetup.py"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>Extern</b></mark></button></form> |

  * `object <module 'inisetup' from 'inisetup.py'> is of type module`
  * `bdev -- <Partition type=1, subtype=129, address=2097152, size=2097152, label=vfs, encrypted=0>`
  * `__name__ -- inisetup`
  * `__file__ -- inisetup.py`
  * `uos -- <module 'uos'>`
  * `fs_corrupted -- <function fs_corrupted at 0x3ffe7980>`
  * `setup -- <function setup at 0x3ffe7990>`
  * `check_bootsec -- <function check_bootsec at 0x3ffe79a0>`

[--> Overview](#Overview)
# math <span id="math"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/math.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'math'> is of type module`
  * `__name__ -- math`
  * `e -- 2.718282`
  * `pi -- 3.141593`
  * `tau -- 6.283185`
  * `inf -- inf`
  * `nan -- nan`
  * `sqrt -- <function>`
  * `pow -- <function>`
  * `exp -- <function>`
  * `expm1 -- <function>`
  * `log -- <function>`
  * `log2 -- <function>`
  * `log10 -- <function>`
  * `cosh -- <function>`
  * `sinh -- <function>`
  * `tanh -- <function>`
  * `acosh -- <function>`
  * `asinh -- <function>`
  * `atanh -- <function>`
  * `cos -- <function>`
  * `sin -- <function>`
  * `tan -- <function>`
  * `acos -- <function>`
  * `asin -- <function>`
  * `atan -- <function>`
  * `atan2 -- <function>`
  * `ceil -- <function>`
  * `copysign -- <function>`
  * `fabs -- <function>`
  * `floor -- <function>`
  * `fmod -- <function>`
  * `frexp -- <function>`
  * `ldexp -- <function>`
  * `modf -- <function>`
  * `isfinite -- <function>`
  * `isinf -- <function>`
  * `isnan -- <function>`
  * `isclose -- <function>`
  * `trunc -- <function>`
  * `radians -- <function>`
  * `degrees -- <function>`
  * `factorial -- <function>`
  * `erf -- <function>`
  * `erfc -- <function>`
  * `gamma -- <function>`
  * `lgamma -- <function>`

[--> Overview](#Overview)
# micropython <span id="micropython"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/micropython.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'micropython'> is of type module`
  * `__name__ -- micropython`
  * `const -- <function>`
  * `opt_level -- <function>`
  * `mem_info -- <function>`
  * `qstr_info -- <function>`
  * `stack_use -- <function>`
  * `alloc_emergency_exception_buf -- <function>`
  * `heap_lock -- <function>`
  * `heap_unlock -- <function>`
  * `kbd_intr -- <function>`
  * `schedule -- <function>`

[--> Overview](#Overview)
# neopixel <span id="neopixel"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/neopixel.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'neopixel' from 'neopixel.py'> is of type module`
  * `bitstream -- <function>`
  * [`NeoPixel -- <class 'NeoPixel'>`](#neopixel.NeoPixel)
  * `__name__ -- neopixel`
  * `__file__ -- neopixel.py`

[--> Overview](#Overview)
## neopixel --> NeoPixel <span id="neopixel.NeoPixel"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/esp32/quickref.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button><input  type="hidden" name="highlight" value="NeoPixel" /> </form> |

  * `ORDER -- (1, 0, 2, 3)`
  * `__getitem__ -- <function __getitem__ at 0x3ffe8e10>`
  * `__init__ -- <function __init__ at 0x3ffe8e20>`
  * `__len__ -- <function __len__ at 0x3ffe8e40>`
  * `__module__ -- neopixel`
  * `__qualname__ -- NeoPixel`
  * `__setitem__ -- <function __setitem__ at 0x3ffe8e00>`
  * `fill -- <function fill at 0x3ffe8e50>`
  * `object <class 'NeoPixel'> is of type type`
  * `write -- <function write at 0x3ffe8e60>`

[--> neopixel](#neopixel)

[--> Overview](#Overview)
# network <span id="network"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/network.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'network'> is of type module`
  * `__name__ -- network`
  * `__init__ -- <function>`
  * `WLAN -- <function>`
  * `LAN -- <function>`
  * `PPP -- <function>`
  * `phy_mode -- <function>`
  * `STA_IF -- 0`
  * `AP_IF -- 1`
  * `MODE_11B -- 1`
  * `MODE_11G -- 2`
  * `MODE_11N -- 4`
  * `AUTH_OPEN -- 0`
  * `AUTH_WEP -- 1`
  * `AUTH_WPA_PSK -- 2`
  * `AUTH_WPA2_PSK -- 3`
  * `AUTH_WPA_WPA2_PSK -- 4`
  * `AUTH_WPA2_ENTERPRISE -- 5`
  * `AUTH_WPA3_PSK -- 6`
  * `AUTH_WPA2_WPA3_PSK -- 7`
  * `AUTH_MAX -- 8`
  * `PHY_LAN8720 -- 0`
  * `PHY_IP101 -- 1`
  * `PHY_RTL8201 -- 2`
  * `PHY_DP83848 -- 3`
  * `ETH_INITIALIZED -- 0`
  * `ETH_STARTED -- 1`
  * `ETH_STOPPED -- 2`
  * `ETH_CONNECTED -- 3`
  * `ETH_DISCONNECTED -- 4`
  * `ETH_GOT_IP -- 5`
  * `STAT_IDLE -- 1000`
  * `STAT_CONNECTING -- 1001`
  * `STAT_GOT_IP -- 1010`
  * `STAT_NO_AP_FOUND -- 201`
  * `STAT_WRONG_PASSWORD -- 202`
  * `STAT_BEACON_TIMEOUT -- 200`
  * `STAT_ASSOC_FAIL -- 203`
  * `STAT_HANDSHAKE_TIMEOUT -- 204`

[--> Overview](#Overview)
# ntptime <span id="ntptime"></span>

|    |    |
| --- | --- |
| <form action="https://bhave.sh/micropython-ntp/"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>Extern</b></mark></button></form> | <form action="https://www.engineersgarage.com/micropython-esp8266-esp32-rtc-utc-local-time/"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>Extern</b></mark></button></form> |

  * `object <module 'ntptime' from 'ntptime.py'> is of type module`
  * `socket -- <module 'usocket'>`
  * `NTP_DELTA -- 3155673600`
  * `struct -- <module 'ustruct'>`
  * `__name__ -- ntptime`
  * `__file__ -- ntptime.py`
  * `host -- pool.ntp.org`
  * `time -- <function time at 0x3ffe7930>`
  * `settime -- <function settime at 0x3ffed280>`

[--> Overview](#Overview)
# onewire <span id="onewire"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/esp32/quickref.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button><input  type="hidden" name="highlight" value="onewire" /> </form> |

  * `object <module 'onewire' from 'onewire.py'> is of type module`
  * `__name__ -- onewire`
  * `_ow -- <module 'onewire'>`
  * [`OneWireError -- <class 'OneWireError'>`](#onewire.OneWireError)
  * `__file__ -- onewire.py`
  * [`OneWire -- <class 'OneWire'>`](#onewire.OneWire)

[--> Overview](#Overview)
## onewire --> OneWireError <span id="onewire.OneWireError"></span>

  * `__module__ -- onewire`
  * `__qualname__ -- OneWireError`
  * `object <class 'OneWireError'> is of type type`

[--> onewire](#onewire)

[--> Overview](#Overview)
## onewire --> OneWire <span id="onewire.OneWire"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/esp32/quickref.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button><input  type="hidden" name="highlight" value="OneWire" /> </form> |

  * `MATCH_ROM -- 85`
  * `SEARCH_ROM -- 240`
  * `SKIP_ROM -- 204`
  * `__init__ -- <function __init__ at 0x3ffedb60>`
  * `__module__ -- onewire`
  * `__qualname__ -- OneWire`
  * `_search_rom -- <function _search_rom at 0x3ffedc20>`
  * `crc8 -- <function crc8 at 0x3ffedc30>`
  * `object <class 'OneWire'> is of type type`
  * `readbit -- <function readbit at 0x3ffedb80>`
  * `readbyte -- <function readbyte at 0x3ffedb90>`
  * `readinto -- <function readinto at 0x3ffedba0>`
  * `reset -- <function reset at 0x3ffedbc0>`
  * `scan -- <function scan at 0x3ffedc10>`
  * `select_rom -- <function select_rom at 0x3ffedc00>`
  * `write -- <function write at 0x3ffedbf0>`
  * `writebit -- <function writebit at 0x3ffedbb0>`
  * `writebyte -- <function writebyte at 0x3ffedbe0>`

[--> onewire](#onewire)

[--> Overview](#Overview)
# uarray <span id="uarray"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/uarray.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'uarray'> is of type module`
  * `__name__ -- uarray`
  * [`array -- <class 'array'>`](#uarray.array)

[--> Overview](#Overview)
## uarray --> array <span id="uarray.array"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/array.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `append -- <function>`
  * `decode -- <function>`
  * `extend -- <function>`
  * `object <class 'array'> is of type type`

[--> uarray](#uarray)

[--> Overview](#Overview)
# uasyncio/core <span id="uasyncio/core"></span>

|    |    |    |
| --- | --- | --- |
| <form action="https://docs.micropython.org/en/latest/library/uasyncio.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> | <form action="https://github.com/peterhinch/micropython-async/blob/master/v3/README.md"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>Extern</b></mark></button></form> | <form action="https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>Extern</b></mark></button></form> |

  * `object <module 'uasyncio/core' from 'uasyncio/core.py'> is of type module`
  * `sys -- <module 'sys'>`
  * [`Task -- <class 'Task'>`](#uasyncio/core.Task)
  * `new_event_loop -- <function new_event_loop at 0x3fff00d0>`
  * `_promote_to_task -- <function _promote_to_task at 0x3fff0050>`
  * `__name__ -- uasyncio/core`
  * `run -- <function run at 0x3ffeff30>`
  * `current_task -- <function current_task at 0x3fff00c0>`
  * `_task_queue -- <TaskQueue>`
  * `_io_queue -- <IOQueue object at 3fff00f0>`
  * `sleep_ms -- <function sleep_ms at 0x3ffefe20>`
  * `sleep -- <function sleep at 0x3ffefe60>`
  * `ticks_add -- <function>`
  * `_exc_context -- {'future': None, 'message': "Task exception wasn't retrieved", 'exception': None}`
  * `ticks_diff -- <function>`
  * [`TaskQueue -- <class 'TaskQueue'>`](#uasyncio/core.TaskQueue)
  * [`SingletonGenerator -- <class 'SingletonGenerator'>`](#uasyncio/core.SingletonGenerator)
  * [`TimeoutError -- <class 'TimeoutError'>`](#uasyncio/core.TimeoutError)
  * `__file__ -- uasyncio/core.py`
  * `_stopper -- <generator>`
  * [`Loop -- <class 'Loop'>`](#uasyncio/core.Loop)
  * [`IOQueue -- <class 'IOQueue'>`](#uasyncio/core.IOQueue)
  * `select -- <module 'uselect'>`
  * `_stop_task -- None`
  * [`CancelledError -- <class 'CancelledError'>`](#uasyncio/core.CancelledError)
  * `get_event_loop -- <function get_event_loop at 0x3fff0240>`
  * `run_until_complete -- <function run_until_complete at 0x3ffeff10>`
  * `ticks -- <function>`
  * `create_task -- <function create_task at 0x3fff00b0>`

[--> Overview](#Overview)
## uasyncio/core --> Task <span id="uasyncio/core.Task"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/uasyncio.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <class 'Task'> is of type type`

[--> uasyncio/core](#uasyncio/core)

[--> Overview](#Overview)
## uasyncio/core --> TaskQueue <span id="uasyncio/core.TaskQueue"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/uasyncio.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <class 'TaskQueue'> is of type type`
  * `peek -- <function>`
  * `pop -- <function>`
  * `push -- <function>`
  * `remove -- <function>`

[--> uasyncio/core](#uasyncio/core)

[--> Overview](#Overview)
## uasyncio/core --> SingletonGenerator <span id="uasyncio/core.SingletonGenerator"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/uasyncio.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `__init__ -- <function __init__ at 0x3ffefe50>`
  * `__iter__ -- <function __iter__ at 0x3ffefe40>`
  * `__module__ -- uasyncio/core`
  * `__next__ -- <function __next__ at 0x3ffefe80>`
  * `__qualname__ -- SingletonGenerator`
  * `object <class 'SingletonGenerator'> is of type type`

[--> uasyncio/core](#uasyncio/core)

[--> Overview](#Overview)
## uasyncio/core --> TimeoutError <span id="uasyncio/core.TimeoutError"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/uasyncio.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `__module__ -- uasyncio/core`
  * `__qualname__ -- TimeoutError`
  * `object <class 'TimeoutError'> is of type type`

[--> uasyncio/core](#uasyncio/core)

[--> Overview](#Overview)
## uasyncio/core --> Loop <span id="uasyncio/core.Loop"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/uasyncio.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `__module__ -- uasyncio/core`
  * `__qualname__ -- Loop`
  * `_exc_handler -- None`
  * `call_exception_handler -- <function call_exception_handler at 0x3fff01e0>`
  * `close -- <function close at 0x3fff01a0>`
  * `create_task -- <function create_task at 0x3ffeff70>`
  * `default_exception_handler -- <function default_exception_handler at 0x3fff01d0>`
  * `get_exception_handler -- <function get_exception_handler at 0x3fff01c0>`
  * `object <class 'Loop'> is of type type`
  * `run_forever -- <function run_forever at 0x3ffeff80>`
  * `run_until_complete -- <function run_until_complete at 0x3fff0180>`
  * `set_exception_handler -- <function set_exception_handler at 0x3fff01b0>`
  * `stop -- <function stop at 0x3fff0190>`

[--> uasyncio/core](#uasyncio/core)

[--> Overview](#Overview)
## uasyncio/core --> IOQueue <span id="uasyncio/core.IOQueue"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/uasyncio.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `__init__ -- <function __init__ at 0x3ffeffb0>`
  * `__module__ -- uasyncio/core`
  * `__qualname__ -- IOQueue`
  * `_dequeue -- <function _dequeue at 0x3ffeffe0>`
  * `_enqueue -- <function _enqueue at 0x3ffeffa0>`
  * `object <class 'IOQueue'> is of type type`
  * `queue_read -- <function queue_read at 0x3ffeffc0>`
  * `queue_write -- <function queue_write at 0x3ffeffd0>`
  * `remove -- <function remove at 0x3ffefff0>`
  * `wait_io_event -- <function wait_io_event at 0x3fff0000>`

[--> uasyncio/core](#uasyncio/core)

[--> Overview](#Overview)
## uasyncio/core --> CancelledError <span id="uasyncio/core.CancelledError"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/uasyncio.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `__module__ -- uasyncio/core`
  * `__qualname__ -- CancelledError`
  * `object <class 'CancelledError'> is of type type`

[--> uasyncio/core](#uasyncio/core)

[--> Overview](#Overview)
# uasyncio/event <span id="uasyncio/event"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/uasyncio.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'ubinascii'> is of type module`
  * `__name__ -- ubinascii`
  * `hexlify -- <function>`
  * `unhexlify -- <function>`
  * `a2b_base64 -- <function>`
  * `b2a_base64 -- <function>`
  * `crc32 -- <function>`

[--> Overview](#Overview)
# ubluetooth <span id="ubluetooth"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/ubluetooth.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'ubluetooth'> is of type module`
  * `__name__ -- ubluetooth`
  * [`BLE -- <class 'BLE'>`](#ubluetooth.BLE)
  * [`UUID -- <class 'UUID'>`](#ubluetooth.UUID)
  * `FLAG_READ -- 2`
  * `FLAG_WRITE -- 8`
  * `FLAG_NOTIFY -- 16`
  * `FLAG_INDICATE -- 32`
  * `FLAG_WRITE_NO_RESPONSE -- 4`

[--> Overview](#Overview)
## ubluetooth --> BLE <span id="ubluetooth.BLE"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/bluetooth.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `active -- <function>`
  * `config -- <function>`
  * `gap_advertise -- <function>`
  * `gap_connect -- <function>`
  * `gap_disconnect -- <function>`
  * `gap_scan -- <function>`
  * `gattc_discover_characteristics -- <function>`
  * `gattc_discover_descriptors -- <function>`
  * `gattc_discover_services -- <function>`
  * `gattc_exchange_mtu -- <function>`
  * `gattc_read -- <function>`
  * `gattc_write -- <function>`
  * `gatts_indicate -- <function>`
  * `gatts_notify -- <function>`
  * `gatts_read -- <function>`
  * `gatts_register_services -- <function>`
  * `gatts_set_buffer -- <function>`
  * `gatts_write -- <function>`
  * `irq -- <function>`
  * `object <class 'BLE'> is of type type`

[--> ubluetooth](#ubluetooth)

[--> Overview](#Overview)
## ubluetooth --> UUID <span id="ubluetooth.UUID"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/bluetooth.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <class 'UUID'> is of type type`

[--> ubluetooth](#ubluetooth)

[--> Overview](#Overview)
# ucollections <span id="ucollections"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/ucollections.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'ucollections'> is of type module`
  * `__name__ -- ucollections`
  * [`deque -- <class 'deque'>`](#ucollections.deque)
  * `namedtuple -- <function>`
  * [`OrderedDict -- <class 'OrderedDict'>`](#ucollections.OrderedDict)

[--> Overview](#Overview)
## ucollections --> deque <span id="ucollections.deque"></span>

|    |    |
| --- | --- |
| <form action="https://docs.micropython.org/en/latest/library/collections.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> | <form action="https://docs.micropython.org/en/latest/library/collections.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="deque" /> </form> |

  * `append -- <function>`
  * `object <class 'deque'> is of type type`
  * `popleft -- <function>`

[--> ucollections](#ucollections)

[--> Overview](#Overview)
## ucollections --> OrderedDict <span id="ucollections.OrderedDict"></span>

|    |    |
| --- | --- |
| <form action="https://docs.micropython.org/en/latest/library/collections.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> | <form action="https://docs.micropython.org/en/latest/library/collections.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="OrderedDict" /> </form> |

  * `__delitem__ -- <function>`
  * `__getitem__ -- <function>`
  * `__setitem__ -- <function>`
  * `clear -- <function>`
  * `copy -- <function>`
  * `fromkeys -- <classmethod>`
  * `get -- <function>`
  * `items -- <function>`
  * `keys -- <function>`
  * `object <class 'OrderedDict'> is of type type`
  * `pop -- <function>`
  * `popitem -- <function>`
  * `setdefault -- <function>`
  * `update -- <function>`
  * `values -- <function>`

[--> ucollections](#ucollections)

[--> Overview](#Overview)
# ucryptolib <span id="ucryptolib"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/ucryptolib.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'ucryptolib'> is of type module`
  * `__name__ -- ucryptolib`
  * [`aes -- <class 'aes'>`](#ucryptolib.aes)

[--> Overview](#Overview)
## ucryptolib --> aes <span id="ucryptolib.aes"></span>

|    |    |    |
| --- | --- | --- |
| <form action="https://docs.micropython.org/en/latest/library/cryptolib.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> | <form action="https://docs.micropython.org/en/latest/library/cryptolib.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP Home highlight</b></mark></button><input  type="hidden" name="highlight" value="aes" /> </form> | <form action="https://hwwong168.wordpress.com/2019/09/25/esp32-micropython-implementation-of-cryptographic/"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>Extern</b></mark></button></form> |

  * `decrypt -- <function>`
  * `encrypt -- <function>`
  * `object <class 'aes'> is of type type`

[--> ucryptolib](#ucryptolib)

[--> Overview](#Overview)
# uctypes <span id="uctypes"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/uctypes.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'uctypes'> is of type module`
  * `__name__ -- uctypes`
  * [`struct -- <class 'struct'>`](#uctypes.struct)
  * `sizeof -- <function>`
  * `addressof -- <function>`
  * `bytes_at -- <function>`
  * `bytearray_at -- <function>`
  * `NATIVE -- 2`
  * `LITTLE_ENDIAN -- 0`
  * `BIG_ENDIAN -- 1`
  * `VOID -- 0`
  * `UINT8 -- 0`
  * `INT8 -- 134217728`
  * `UINT16 -- 268435456`
  * `INT16 -- 402653184`
  * `UINT32 -- 536870912`
  * `INT32 -- 671088640`
  * `UINT64 -- 805306368`
  * `INT64 -- 939524096`
  * `BFUINT8 -- -1073741824`
  * `BFINT8 -- -939524096`
  * `BFUINT16 -- -805306368`
  * `BFINT16 -- -671088640`
  * `BFUINT32 -- -536870912`
  * `BFINT32 -- -402653184`
  * `BF_POS -- 17`
  * `BF_LEN -- 22`
  * `FLOAT32 -- -268435456`
  * `FLOAT64 -- -134217728`
  * `SHORT -- 402653184`
  * `USHORT -- 268435456`
  * `INT -- 671088640`
  * `UINT -- 536870912`
  * `LONG -- 671088640`
  * `ULONG -- 536870912`
  * `LONGLONG -- 939524096`
  * `ULONGLONG -- 805306368`
  * `PTR -- 536870912`
  * `ARRAY -- -1073741824`

[--> Overview](#Overview)
## uctypes --> struct <span id="uctypes.struct"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/esp32/quickref.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button><input  type="hidden" name="highlight" value="struct" /> </form> |

  * `object <class 'struct'> is of type type`

[--> uctypes](#uctypes)

[--> Overview](#Overview)
# uerrno <span id="uerrno"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/uerrno.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'uerrno'> is of type module`
  * `__name__ -- uerrno`
  * `errorcode -- {1: 'EPERM', 2: 'ENOENT', 5: 'EIO', 9: 'EBADF', 11: 'EAGAIN', 12: 'ENOMEM', 13: 'EACCES', 17: 'EEXIST', 19: 'ENODEV', 21: 'EISDIR', 22: 'EINVAL', 95: 'EOPNOTSUPP', 112: 'EADDRINUSE', 113: 'ECONNABORTED', 104: 'ECONNRESET', 105: 'ENOBUFS', 128: 'ENOTCONN', 116: 'ETIMEDOUT', 111: 'ECONNREFUSED', 118: 'EHOSTUNREACH', 120: 'EALREADY', 119: 'EINPROGRESS'}`
  * `EPERM -- 1`
  * `ENOENT -- 2`
  * `EIO -- 5`
  * `EBADF -- 9`
  * `EAGAIN -- 11`
  * `ENOMEM -- 12`
  * `EACCES -- 13`
  * `EEXIST -- 17`
  * `ENODEV -- 19`
  * `EISDIR -- 21`
  * `EINVAL -- 22`
  * `EOPNOTSUPP -- 95`
  * `EADDRINUSE -- 112`
  * `ECONNABORTED -- 113`
  * `ECONNRESET -- 104`
  * `ENOBUFS -- 105`
  * `ENOTCONN -- 128`
  * `ETIMEDOUT -- 116`
  * `ECONNREFUSED -- 111`
  * `EHOSTUNREACH -- 118`
  * `EALREADY -- 120`
  * `EINPROGRESS -- 119`

[--> Overview](#Overview)
# uhashlib <span id="uhashlib"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/uhashlib.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'uhashlib'> is of type module`
  * `__name__ -- uhashlib`
  * [`sha256 -- <class 'sha256'>`](#uhashlib.sha256)
  * [`sha1 -- <class 'sha1'>`](#uhashlib.sha1)

[--> Overview](#Overview)
## uhashlib --> sha256 <span id="uhashlib.sha256"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/hashlib.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `digest -- <function>`
  * `object <class 'sha256'> is of type type`
  * `update -- <function>`

[--> uhashlib](#uhashlib)

[--> Overview](#Overview)
## uhashlib --> sha1 <span id="uhashlib.sha1"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/hashlib.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `digest -- <function>`
  * `object <class 'sha1'> is of type type`
  * `update -- <function>`

[--> uhashlib](#uhashlib)

[--> Overview](#Overview)
# uheapq <span id="uheapq"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/uheapq.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'uheapq'> is of type module`
  * `__name__ -- uheapq`
  * `heappush -- <function>`
  * `heappop -- <function>`
  * `heapify -- <function>`

[--> Overview](#Overview)
# uio <span id="uio"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/uio.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'uio'> is of type module`
  * `__name__ -- uio`
  * `open -- <function>`
  * [`IOBase -- <class 'IOBase'>`](#uio.IOBase)
  * [`FileIO -- <class 'FileIO'>`](#uio.FileIO)
  * [`TextIOWrapper -- <class 'TextIOWrapper'>`](#uio.TextIOWrapper)
  * [`StringIO -- <class 'StringIO'>`](#uio.StringIO)
  * [`BytesIO -- <class 'BytesIO'>`](#uio.BytesIO)
  * [`BufferedWriter -- <class 'BufferedWriter'>`](#uio.BufferedWriter)

[--> Overview](#Overview)
## uio --> IOBase <span id="uio.IOBase"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/io.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <class 'IOBase'> is of type type`

[--> uio](#uio)

[--> Overview](#Overview)
## uio --> FileIO <span id="uio.FileIO"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/io.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `__del__ -- <function>`
  * `__enter__ -- <function>`
  * `__exit__ -- <function>`
  * `close -- <function>`
  * `flush -- <function>`
  * `object <class 'FileIO'> is of type type`
  * `read -- <function>`
  * `readinto -- <function>`
  * `readline -- <function>`
  * `readlines -- <function>`
  * `seek -- <function>`
  * `tell -- <function>`
  * `write -- <function>`

[--> uio](#uio)

[--> Overview](#Overview)
## uio --> TextIOWrapper <span id="uio.TextIOWrapper"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/io.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `__del__ -- <function>`
  * `__enter__ -- <function>`
  * `__exit__ -- <function>`
  * `close -- <function>`
  * `flush -- <function>`
  * `object <class 'TextIOWrapper'> is of type type`
  * `read -- <function>`
  * `readinto -- <function>`
  * `readline -- <function>`
  * `readlines -- <function>`
  * `seek -- <function>`
  * `tell -- <function>`
  * `write -- <function>`

[--> uio](#uio)

[--> Overview](#Overview)
## uio --> StringIO <span id="uio.StringIO"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/io.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `__enter__ -- <function>`
  * `__exit__ -- <function>`
  * `close -- <function>`
  * `flush -- <function>`
  * `getvalue -- <function>`
  * `object <class 'StringIO'> is of type type`
  * `read -- <function>`
  * `readinto -- <function>`
  * `readline -- <function>`
  * `seek -- <function>`
  * `tell -- <function>`
  * `write -- <function>`

[--> uio](#uio)

[--> Overview](#Overview)
## uio --> BytesIO <span id="uio.BytesIO"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/io.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `__enter__ -- <function>`
  * `__exit__ -- <function>`
  * `close -- <function>`
  * `flush -- <function>`
  * `getvalue -- <function>`
  * `object <class 'BytesIO'> is of type type`
  * `read -- <function>`
  * `readinto -- <function>`
  * `readline -- <function>`
  * `seek -- <function>`
  * `tell -- <function>`
  * `write -- <function>`

[--> uio](#uio)

[--> Overview](#Overview)
## uio --> BufferedWriter <span id="uio.BufferedWriter"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/io.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `flush -- <function>`
  * `object <class 'BufferedWriter'> is of type type`
  * `write -- <function>`

[--> uio](#uio)

[--> Overview](#Overview)
# ujson <span id="ujson"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/ujson.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'ujson'> is of type module`
  * `__name__ -- ujson`
  * `dump -- <function>`
  * `dumps -- <function>`
  * `load -- <function>`
  * `loads -- <function>`

[--> Overview](#Overview)
# umachine <span id="umachine"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'umachine'> is of type module`
  * `__name__ -- umachine`
  * `mem8 -- <8-bit memory>`
  * `mem16 -- <16-bit memory>`
  * `mem32 -- <32-bit memory>`
  * `freq -- <function>`
  * `reset -- <function>`
  * `soft_reset -- <function>`
  * `unique_id -- <function>`
  * `sleep -- <function>`
  * `lightsleep -- <function>`
  * `deepsleep -- <function>`
  * `idle -- <function>`
  * `disable_irq -- <function>`
  * `enable_irq -- <function>`
  * `bitstream -- <function>`
  * `time_pulse_us -- <function>`
  * [`Timer -- <class 'Timer'>`](#umachine.Timer)
  * [`WDT -- <class 'WDT'>`](#umachine.WDT)
  * [`SDCard -- <class 'SDCard'>`](#umachine.SDCard)
  * `SLEEP -- 2`
  * `DEEPSLEEP -- 4`
  * [`Pin -- <class 'Pin'>`](#umachine.Pin)
  * [`Signal -- <class 'Signal'>`](#umachine.Signal)
  * [`TouchPad -- <class 'TouchPad'>`](#umachine.TouchPad)
  * [`ADC -- <class 'ADC'>`](#umachine.ADC)
  * [`ADCBlock -- <class 'ADCBlock'>`](#umachine.ADCBlock)
  * [`DAC -- <class 'DAC'>`](#umachine.DAC)
  * [`I2C -- <class 'I2C'>`](#umachine.I2C)
  * [`SoftI2C -- <class 'SoftI2C'>`](#umachine.SoftI2C)
  * [`I2S -- <class 'I2S'>`](#umachine.I2S)
  * [`PWM -- <class 'PWM'>`](#umachine.PWM)
  * [`RTC -- <class 'RTC'>`](#umachine.RTC)
  * [`SPI -- <class 'SPI'>`](#umachine.SPI)
  * [`SoftSPI -- <class 'SoftSPI'>`](#umachine.SoftSPI)
  * [`UART -- <class 'UART'>`](#umachine.UART)
  * `reset_cause -- <function>`
  * `HARD_RESET -- 2`
  * `PWRON_RESET -- 1`
  * `WDT_RESET -- 3`
  * `DEEPSLEEP_RESET -- 4`
  * `SOFT_RESET -- 5`
  * `wake_reason -- <function>`
  * `PIN_WAKE -- 2`
  * `EXT0_WAKE -- 2`
  * `EXT1_WAKE -- 3`
  * `TIMER_WAKE -- 4`
  * `TOUCHPAD_WAKE -- 5`
  * `ULP_WAKE -- 6`

[--> Overview](#Overview)
## umachine --> Timer <span id="umachine.Timer"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `ONE_SHOT -- 0`
  * `PERIODIC -- 1`
  * `__del__ -- <function>`
  * `deinit -- <function>`
  * `init -- <function>`
  * `object <class 'Timer'> is of type type`
  * `value -- <function>`

[--> umachine](#umachine)

[--> Overview](#Overview)
## umachine --> WDT <span id="umachine.WDT"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `feed -- <function>`
  * `object <class 'WDT'> is of type type`

[--> umachine](#umachine)

[--> Overview](#Overview)
## umachine --> SDCard <span id="umachine.SDCard"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `__del__ -- <function>`
  * `deinit -- <function>`
  * `info -- <function>`
  * `ioctl -- <function>`
  * `object <class 'SDCard'> is of type type`
  * `readblocks -- <function>`
  * `writeblocks -- <function>`

[--> umachine](#umachine)

[--> Overview](#Overview)
## umachine --> Pin <span id="umachine.Pin"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `DRIVE_0 -- 0`
  * `DRIVE_1 -- 1`
  * `DRIVE_2 -- 2`
  * `DRIVE_3 -- 3`
  * `IN -- 1`
  * `IRQ_FALLING -- 2`
  * `IRQ_RISING -- 1`
  * `OPEN_DRAIN -- 7`
  * `OUT -- 3`
  * `PULL_DOWN -- 1`
  * `PULL_UP -- 2`
  * `WAKE_HIGH -- 5`
  * `WAKE_LOW -- 4`
  * `init -- <function>`
  * `irq -- <function>`
  * `object <class 'Pin'> is of type type`
  * `off -- <function>`
  * `on -- <function>`
  * `value -- <function>`

[--> umachine](#umachine)

[--> Overview](#Overview)
## umachine --> Signal <span id="umachine.Signal"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <class 'Signal'> is of type type`
  * `off -- <function>`
  * `on -- <function>`
  * `value -- <function>`

[--> umachine](#umachine)

[--> Overview](#Overview)
## umachine --> TouchPad <span id="umachine.TouchPad"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `config -- <function>`
  * `object <class 'TouchPad'> is of type type`
  * `read -- <function>`

[--> umachine](#umachine)

[--> Overview](#Overview)
## umachine --> ADC <span id="umachine.ADC"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `ATTN_0DB -- 0`
  * `ATTN_11DB -- 3`
  * `ATTN_2_5DB -- 1`
  * `ATTN_6DB -- 2`
  * `WIDTH_10BIT -- 10`
  * `WIDTH_11BIT -- 11`
  * `WIDTH_12BIT -- 12`
  * `WIDTH_9BIT -- 9`
  * `atten -- <function>`
  * `block -- <function>`
  * `init -- <function>`
  * `object <class 'ADC'> is of type type`
  * `read -- <function>`
  * `read_u16 -- <function>`
  * `read_uv -- <function>`
  * `width -- <function>`

[--> umachine](#umachine)

[--> Overview](#Overview)
## umachine --> ADCBlock <span id="umachine.ADCBlock"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `connect -- <function>`
  * `init -- <function>`
  * `object <class 'ADCBlock'> is of type type`

[--> umachine](#umachine)

[--> Overview](#Overview)
## umachine --> DAC <span id="umachine.DAC"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <class 'DAC'> is of type type`
  * `write -- <function>`

[--> umachine](#umachine)

[--> Overview](#Overview)
## umachine --> I2C <span id="umachine.I2C"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `init -- <function>`
  * `object <class 'I2C'> is of type type`
  * `readfrom -- <function>`
  * `readfrom_into -- <function>`
  * `readfrom_mem -- <function>`
  * `readfrom_mem_into -- <function>`
  * `readinto -- <function>`
  * `scan -- <function>`
  * `start -- <function>`
  * `stop -- <function>`
  * `write -- <function>`
  * `writeto -- <function>`
  * `writeto_mem -- <function>`
  * `writevto -- <function>`

[--> umachine](#umachine)

[--> Overview](#Overview)
## umachine --> SoftI2C <span id="umachine.SoftI2C"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `init -- <function>`
  * `object <class 'SoftI2C'> is of type type`
  * `readfrom -- <function>`
  * `readfrom_into -- <function>`
  * `readfrom_mem -- <function>`
  * `readfrom_mem_into -- <function>`
  * `readinto -- <function>`
  * `scan -- <function>`
  * `start -- <function>`
  * `stop -- <function>`
  * `write -- <function>`
  * `writeto -- <function>`
  * `writeto_mem -- <function>`
  * `writevto -- <function>`

[--> umachine](#umachine)

[--> Overview](#Overview)
## umachine --> I2S <span id="umachine.I2S"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `MONO -- 0`
  * `RX -- 9`
  * `STEREO -- 1`
  * `TX -- 5`
  * `deinit -- <function>`
  * `init -- <function>`
  * `irq -- <function>`
  * `object <class 'I2S'> is of type type`
  * `readinto -- <function>`
  * `shift -- <staticmethod>`
  * `write -- <function>`

[--> umachine](#umachine)

[--> Overview](#Overview)
## umachine --> PWM <span id="umachine.PWM"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `deinit -- <function>`
  * `duty -- <function>`
  * `duty_ns -- <function>`
  * `duty_u16 -- <function>`
  * `freq -- <function>`
  * `init -- <function>`
  * `object <class 'PWM'> is of type type`

[--> umachine](#umachine)

[--> Overview](#Overview)
## umachine --> RTC <span id="umachine.RTC"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `datetime -- <function>`
  * `init -- <function>`
  * `memory -- <function>`
  * `object <class 'RTC'> is of type type`

[--> umachine](#umachine)

[--> Overview](#Overview)
## umachine --> SPI <span id="umachine.SPI"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `LSB -- 1`
  * `MSB -- 0`
  * `deinit -- <function>`
  * `init -- <function>`
  * `object <class 'SPI'> is of type type`
  * `read -- <function>`
  * `readinto -- <function>`
  * `write -- <function>`
  * `write_readinto -- <function>`

[--> umachine](#umachine)

[--> Overview](#Overview)
## umachine --> SoftSPI <span id="umachine.SoftSPI"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `LSB -- 1`
  * `MSB -- 0`
  * `deinit -- <function>`
  * `init -- <function>`
  * `object <class 'SoftSPI'> is of type type`
  * `read -- <function>`
  * `readinto -- <function>`
  * `write -- <function>`
  * `write_readinto -- <function>`

[--> umachine](#umachine)

[--> Overview](#Overview)
## umachine --> UART <span id="umachine.UART"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/machine.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `CTS -- 2`
  * `INV_CTS -- 8`
  * `INV_RTS -- 64`
  * `INV_RX -- 4`
  * `INV_TX -- 32`
  * `RTS -- 1`
  * `any -- <function>`
  * `deinit -- <function>`
  * `init -- <function>`
  * `object <class 'UART'> is of type type`
  * `read -- <function>`
  * `readinto -- <function>`
  * `readline -- <function>`
  * `sendbreak -- <function>`
  * `write -- <function>`

[--> umachine](#umachine)

[--> Overview](#Overview)
# umqtt/robust <span id="umqtt/robust"></span>

  * `object <module 'umqtt/simple' from 'umqtt/simple.py'> is of type module`
  * `socket -- <module 'usocket'>`
  * [`MQTTClient -- <class 'MQTTClient'>`](#umqtt/simple.MQTTClient)
  * `struct -- <module 'ustruct'>`
  * `__name__ -- umqtt/simple`
  * `__file__ -- umqtt/simple.py`
  * `hexlify -- <function>`
  * [`MQTTException -- <class 'MQTTException'>`](#umqtt/simple.MQTTException)

[--> Overview](#Overview)
## umqtt/simple --> MQTTClient <span id="umqtt/simple.MQTTClient"></span>

  * `__init__ -- <function __init__ at 0x3ffeec70>`
  * `__module__ -- umqtt/simple`
  * `__qualname__ -- MQTTClient`
  * `_recv_len -- <function _recv_len at 0x3ffeecc0>`
  * `_send_str -- <function _send_str at 0x3ffeec30>`
  * `check_msg -- <function check_msg at 0x3ffeedb0>`
  * `connect -- <function connect at 0x3ffeece0>`
  * `disconnect -- <function disconnect at 0x3ffeed60>`
  * `object <class 'MQTTClient'> is of type type`
  * `ping -- <function ping at 0x3ffeed20>`
  * `publish -- <function publish at 0x3ffeed40>`
  * `set_callback -- <function set_callback at 0x3ffeeca0>`
  * `set_last_will -- <function set_last_will at 0x3ffeed00>`
  * `subscribe -- <function subscribe at 0x3ffeed80>`
  * `wait_msg -- <function wait_msg at 0x3ffeeda0>`

[--> umqtt/simple](#umqtt/simple)

[--> Overview](#Overview)
## umqtt/simple --> MQTTException <span id="umqtt/simple.MQTTException"></span>

  * `__module__ -- umqtt/simple`
  * `__qualname__ -- MQTTException`
  * `object <class 'MQTTException'> is of type type`

[--> umqtt/simple](#umqtt/simple)

[--> Overview](#Overview)
# uos <span id="uos"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/uos.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'uos'> is of type module`
  * `__name__ -- uos`
  * `uname -- <function>`
  * `urandom -- <function>`
  * `chdir -- <function>`
  * `getcwd -- <function>`
  * `listdir -- <function>`
  * `mkdir -- <function>`
  * `remove -- <function>`
  * `rename -- <function>`
  * `rmdir -- <function>`
  * `stat -- <function>`
  * `statvfs -- <function>`
  * `unlink -- <function>`
  * `dupterm -- <function>`
  * `dupterm_notify -- <function>`
  * `ilistdir -- <function>`
  * `mount -- <function>`
  * `umount -- <function>`
  * [`VfsFat -- <class 'VfsFat'>`](#uos.VfsFat)
  * [`VfsLfs2 -- <class 'VfsLfs2'>`](#uos.VfsLfs2)

[--> Overview](#Overview)
## uos --> VfsFat <span id="uos.VfsFat"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/os.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `chdir -- <function>`
  * `getcwd -- <function>`
  * `ilistdir -- <function>`
  * `mkdir -- <function>`
  * `mkfs -- <staticmethod>`
  * `mount -- <function>`
  * `object <class 'VfsFat'> is of type type`
  * `open -- <function>`
  * `remove -- <function>`
  * `rename -- <function>`
  * `rmdir -- <function>`
  * `stat -- <function>`
  * `statvfs -- <function>`
  * `umount -- <function>`

[--> uos](#uos)

[--> Overview](#Overview)
## uos --> VfsLfs2 <span id="uos.VfsLfs2"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/os.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `chdir -- <function>`
  * `getcwd -- <function>`
  * `ilistdir -- <function>`
  * `mkdir -- <function>`
  * `mkfs -- <staticmethod>`
  * `mount -- <function>`
  * `object <class 'VfsLfs2'> is of type type`
  * `open -- <function>`
  * `remove -- <function>`
  * `rename -- <function>`
  * `rmdir -- <function>`
  * `stat -- <function>`
  * `statvfs -- <function>`
  * `umount -- <function>`

[--> uos](#uos)

[--> Overview](#Overview)
# upip <span id="upip"></span>

  * `object <module 'upip' from 'upip.py'> is of type module`
  * `main -- <function main at 0x3ffe5520>`
  * `url_open -- <function url_open at 0x3ffe51c0>`
  * `fatal -- <function fatal at 0x3ffe51f0>`
  * `ussl -- <module 'ussl'>`
  * `usocket -- <module 'usocket'>`
  * `_makedirs -- <function _makedirs at 0x3ffe52e0>`
  * `save_file -- <function save_file at 0x3ffe5190>`
  * [`NotFoundError -- <class 'NotFoundError'>`](#upip.NotFoundError)
  * `os -- <module 'uos'>`
  * `expandhome -- <function expandhome at 0x3ffe51b0>`
  * `__file__ -- upip.py`
  * `cleanup_files -- []`
  * `uzlib -- <module 'uzlib'>`
  * `tarfile -- <module 'upip_utarfile' from 'upip_utarfile.py'>`
  * `install -- <function install at 0x3ffe5440>`
  * `install_path -- None`
  * `index_urls -- ['https://micropython.org/pi', 'https://pypi.org/pypi']`
  * `sys -- <module 'sys'>`
  * `__name__ -- upip`
  * `install_pkg -- <function install_pkg at 0x3ffe5210>`
  * `get_pkg_metadata -- <function get_pkg_metadata at 0x3ffe51d0>`
  * `cleanup -- <function cleanup at 0x3ffe5500>`
  * `gc -- <module 'gc'>`
  * `file_buf -- bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')`
  * `help -- <function help at 0x3ffe5510>`
  * `gzdict_sz -- 31`
  * `op_split -- <function op_split at 0x3ffe5220>`
  * `debug -- False`
  * `errno -- <module 'uerrno'>`
  * `install_tar -- <function install_tar at 0x3ffe51a0>`
  * `json -- <module 'ujson'>`
  * `warn_ussl -- True`
  * `get_install_path -- <function get_install_path at 0x3ffe5460>`

[--> Overview](#Overview)
## upip --> NotFoundError <span id="upip.NotFoundError"></span>

  * `__module__ -- upip`
  * `__qualname__ -- NotFoundError`
  * `object <class 'NotFoundError'> is of type type`

[--> upip](#upip)

[--> Overview](#Overview)
# upip_utarfile <span id="upip_utarfile"></span>

  * `object <module 'upip_utarfile' from 'upip_utarfile.py'> is of type module`
  * [`FileSection -- <class 'FileSection'>`](#upip_utarfile.FileSection)
  * [`TarInfo -- <class 'TarInfo'>`](#upip_utarfile.TarInfo)
  * `__name__ -- upip_utarfile`
  * [`TarFile -- <class 'TarFile'>`](#upip_utarfile.TarFile)
  * `DIRTYPE -- dir`
  * `TAR_HEADER -- {'name': (-1073741824, 100), 'size': (-1073741700, 11)}`
  * `uctypes -- <module 'uctypes'>`
  * `__file__ -- upip_utarfile.py`
  * `roundup -- <function roundup at 0x3fff2f30>`
  * `REGTYPE -- file`

[--> Overview](#Overview)
## upip_utarfile --> FileSection <span id="upip_utarfile.FileSection"></span>

  * `__init__ -- <function __init__ at 0x3fff2fe0>`
  * `__module__ -- upip_utarfile`
  * `__qualname__ -- FileSection`
  * `object <class 'FileSection'> is of type type`
  * `read -- <function read at 0x3fff3050>`
  * `readinto -- <function readinto at 0x3fff3070>`
  * `skip -- <function skip at 0x3fff3030>`

[--> upip_utarfile](#upip_utarfile)

[--> Overview](#Overview)
## upip_utarfile --> TarInfo <span id="upip_utarfile.TarInfo"></span>

  * `__module__ -- upip_utarfile`
  * `__qualname__ -- TarInfo`
  * `__str__ -- <function __str__ at 0x3fff3110>`
  * `object <class 'TarInfo'> is of type type`

[--> upip_utarfile](#upip_utarfile)

[--> Overview](#Overview)
## upip_utarfile --> TarFile <span id="upip_utarfile.TarFile"></span>

  * `__init__ -- <function __init__ at 0x3fff31d0>`
  * `__iter__ -- <function __iter__ at 0x3fff3100>`
  * `__module__ -- upip_utarfile`
  * `__next__ -- <function __next__ at 0x3fff31f0>`
  * `__qualname__ -- TarFile`
  * `extractfile -- <function extractfile at 0x3fff3200>`
  * `next -- <function next at 0x3fff3010>`
  * `object <class 'TarFile'> is of type type`

[--> upip_utarfile](#upip_utarfile)

[--> Overview](#Overview)
# uplatform <span id="uplatform"></span>

  * `object <module 'uplatform'> is of type module`
  * `__name__ -- uplatform`
  * `platform -- <function>`
  * `python_compiler -- <function>`
  * `libc_ver -- <function>`

[--> Overview](#Overview)
# upysh <span id="upysh"></span>

  * `upysh is intended to be imported using:`
  * `from upysh import *`
  * `To see this help text again, type "man".`
  * `upysh commands:`
  * `pwd, cd("new_dir"), ls, ls(...), head(...), cat(...)`
  * `newfile(...), mv("old", "new"), rm(...), mkdir(...), rmdir(...),`
  * `clear`
  * `object <module 'upysh' from 'upysh.py'> is of type module`
  * `man --`
  * `upysh is intended to be imported using:`
  * `from upysh import *`
  * `To see this help text again, type "man".`
  * `upysh commands:`
  * `pwd, cd("new_dir"), ls, ls(...), head(...), cat(...)`
  * `newfile(...), mv("old", "new"), rm(...), mkdir(...), rmdir(...),`
  * `clear`
  * `ls --       29 boot.py`
  * `448 main.py`
  * `1047 micropython_help.txt`
  * `1057 micropython_help_02.txt`
  * `1047 micropython_help_05.txt`
  * `1463 micropython_help_06.txt`
  * `0 python_help.txt`
  * `__file__ -- upysh.py`
  * `rm -- <function>`
  * `cd -- <function>`
  * `__name__ -- upysh`
  * `clear --`
  * `pwd -- /`
  * [`Man -- <class 'Man'>`](#upysh.Man)
  * `mkdir -- <function>`
  * `head -- <function head at 0x3ffed010>`
  * [`CLEAR -- <class 'CLEAR'>`](#upysh.CLEAR)
  * `cat -- <function cat at 0x3ffed030>`
  * `mv -- <function>`
  * `sys -- <module 'sys'>`
  * `os -- <module 'uos'>`
  * `rmdir -- <function>`
  * [`PWD -- <class 'PWD'>`](#upysh.PWD)
  * `newfile -- <function newfile at 0x3ffed040>`
  * [`LS -- <class 'LS'>`](#upysh.LS)

[--> Overview](#Overview)
## upysh --> Man <span id="upysh.Man"></span>

  * `__module__ -- upysh`
  * `__qualname__ -- Man`
  * `__repr__ -- <function __repr__ at 0x3ffecfa0>`
  * `object <class 'Man'> is of type type`

[--> upysh](#upysh)

[--> Overview](#Overview)
## upysh --> CLEAR <span id="upysh.CLEAR"></span>

  * `__call__ -- <function __call__ at 0x3ffecef0>`
  * `__module__ -- upysh`
  * `__qualname__ -- CLEAR`
  * `__repr__ -- <function __repr__ at 0x3ffecf00>`
  * `object <class 'CLEAR'> is of type type`

[--> upysh](#upysh)

[--> Overview](#Overview)
## upysh --> PWD <span id="upysh.PWD"></span>

  * `__call__ -- <function __call__ at 0x3ffece50>`
  * `__module__ -- upysh`
  * `__qualname__ -- PWD`
  * `__repr__ -- <function __repr__ at 0x3ffece60>`
  * `object <class 'PWD'> is of type type`

[--> upysh](#upysh)

[--> Overview](#Overview)
## upysh --> LS <span id="upysh.LS"></span>

  * `__call__ -- <function __call__ at 0x3ffecdc0>`
  * `__module__ -- upysh`
  * `__qualname__ -- LS`
  * `__repr__ -- <function __repr__ at 0x3ffecd90>`
  * `object <class 'LS'> is of type type`

[--> upysh](#upysh)

[--> Overview](#Overview)
# urandom <span id="urandom"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/random.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'urandom'> is of type module`
  * `__name__ -- urandom`
  * `__init__ -- <function>`
  * `getrandbits -- <function>`
  * `seed -- <function>`
  * `randrange -- <function>`
  * `randint -- <function>`
  * `choice -- <function>`
  * `random -- <function>`
  * `uniform -- <function>`

[--> Overview](#Overview)
# ure <span id="ure"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/ure.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'ure'> is of type module`
  * `__name__ -- ure`
  * `compile -- <function>`
  * `match -- <function>`
  * `search -- <function>`
  * `sub -- <function>`

[--> Overview](#Overview)
# urequests <span id="urequests"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/esp32/quickref.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button><input  type="hidden" name="highlight" value="urequests" /> </form> |

  * `object <module 'urequests' from 'urequests.py'> is of type module`
  * `put -- <function put at 0x3fff24e0>`
  * `post -- <function post at 0x3fff24d0>`
  * `usocket -- <module 'usocket'>`
  * `patch -- <function patch at 0x3fff24f0>`
  * `request -- <function request at 0x3fff24b0>`
  * `__file__ -- urequests.py`
  * `__name__ -- urequests`
  * `delete -- <function delete at 0x3fff2500>`
  * `head -- <function head at 0x3fff2360>`
  * [`Response -- <class 'Response'>`](#urequests.Response)
  * `get -- <function get at 0x3fff2370>`

[--> Overview](#Overview)
## urequests --> Response <span id="urequests.Response"></span>

  * `__init__ -- <function __init__ at 0x3fff23a0>`
  * `__module__ -- urequests`
  * `__qualname__ -- Response`
  * `close -- <function close at 0x3fff2390>`
  * `content -- <property>`
  * `json -- <function json at 0x3fff2420>`
  * `object <class 'Response'> is of type type`
  * `text -- <property>`

[--> urequests](#urequests)

[--> Overview](#Overview)
# uselect <span id="uselect"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/uselect.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'uselect'> is of type module`
  * `__name__ -- uselect`
  * `select -- <function>`
  * `poll -- <function>`
  * `POLLIN -- 1`
  * `POLLOUT -- 4`
  * `POLLERR -- 8`
  * `POLLHUP -- 16`

[--> Overview](#Overview)
# usocket <span id="usocket"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/usocket.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'usocket'> is of type module`
  * `__name__ -- usocket`
  * `__init__ -- <function>`
  * [`socket -- <class 'socket'>`](#usocket.socket)
  * `getaddrinfo -- <function>`
  * `AF_INET -- 2`
  * `AF_INET6 -- 10`
  * `SOCK_STREAM -- 1`
  * `SOCK_DGRAM -- 2`
  * `SOCK_RAW -- 3`
  * `IPPROTO_TCP -- 6`
  * `IPPROTO_UDP -- 17`
  * `IPPROTO_IP -- 0`
  * `SOL_SOCKET -- 4095`
  * `SO_REUSEADDR -- 4`
  * `IP_ADD_MEMBERSHIP -- 3`

[--> Overview](#Overview)
## usocket --> socket <span id="usocket.socket"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/socket.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `__del__ -- <function>`
  * `accept -- <function>`
  * `bind -- <function>`
  * `close -- <function>`
  * `connect -- <function>`
  * `fileno -- <function>`
  * `listen -- <function>`
  * `makefile -- <function>`
  * `object <class 'socket'> is of type type`
  * `read -- <function>`
  * `readinto -- <function>`
  * `readline -- <function>`
  * `recv -- <function>`
  * `recvfrom -- <function>`
  * `send -- <function>`
  * `sendall -- <function>`
  * `sendto -- <function>`
  * `setblocking -- <function>`
  * `setsockopt -- <function>`
  * `settimeout -- <function>`
  * `write -- <function>`

[--> usocket](#usocket)

[--> Overview](#Overview)
# ussl <span id="ussl"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/ussl.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'ussl'> is of type module`
  * `__name__ -- ussl`
  * `wrap_socket -- <function>`

[--> Overview](#Overview)
# ustruct <span id="ustruct"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/ustruct.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'ustruct'> is of type module`
  * `__name__ -- ustruct`
  * `calcsize -- <function>`
  * `pack -- <function>`
  * `pack_into -- <function>`
  * `unpack -- <function>`
  * `unpack_from -- <function>`

[--> Overview](#Overview)
# usys <span id="usys"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/usys.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

Hile in Micropython hat fehlgeschlagen


[--> Overview](#Overview)
# utime <span id="utime"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/utime.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'utime'> is of type module`
  * `__name__ -- utime`
  * `gmtime -- <function>`
  * `localtime -- <function>`
  * `mktime -- <function>`
  * `time -- <function>`
  * `sleep -- <function>`
  * `sleep_ms -- <function>`
  * `sleep_us -- <function>`
  * `ticks_ms -- <function>`
  * `ticks_us -- <function>`
  * `ticks_cpu -- <function>`
  * `ticks_add -- <function>`
  * `ticks_diff -- <function>`
  * `time_ns -- <function>`

[--> Overview](#Overview)
# utimeq <span id="utimeq"></span>

  * `object <module 'utimeq'> is of type module`
  * `__name__ -- utimeq`
  * [`utimeq -- <class 'utimeq'>`](#utimeq.utimeq)

[--> Overview](#Overview)
## utimeq --> utimeq <span id="utimeq.utimeq"></span>

  * `object <class 'utimeq'> is of type type`
  * `peektime -- <function>`
  * `pop -- <function>`
  * `push -- <function>`

[--> utimeq](#utimeq)

[--> Overview](#Overview)
# uwebsocket <span id="uwebsocket"></span>

  * `object <module 'uwebsocket'> is of type module`
  * `__name__ -- uwebsocket`
  * [`websocket -- <class 'websocket'>`](#uwebsocket.websocket)

[--> Overview](#Overview)
## uwebsocket --> websocket <span id="uwebsocket.websocket"></span>

  * `close -- <function>`
  * `ioctl -- <function>`
  * `object <class 'websocket'> is of type type`
  * `read -- <function>`
  * `readinto -- <function>`
  * `readline -- <function>`
  * `write -- <function>`

[--> uwebsocket](#uwebsocket)

[--> Overview](#Overview)
# uzlib <span id="uzlib"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/uzlib.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <module 'uzlib'> is of type module`
  * `__name__ -- uzlib`
  * `decompress -- <function>`
  * [`DecompIO -- <class 'DecompIO'>`](#uzlib.DecompIO)

[--> Overview](#Overview)
## uzlib --> DecompIO <span id="uzlib.DecompIO"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/library/zlib.html"  target="_blank"><button type="submit"><mark style="background: SkyBlue;"><b>MP Home</b></mark></button></form> |

  * `object <class 'DecompIO'> is of type type`
  * `read -- <function>`
  * `readinto -- <function>`
  * `readline -- <function>`

[--> uzlib](#uzlib)

[--> Overview](#Overview)
# webrepl <span id="webrepl"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/esp32/quickref.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button><input  type="hidden" name="highlight" value="webrepl" /> </form> |

Hile in Micropython hat fehlgeschlagen


[--> Overview](#Overview)
# webrepl_setup <span id="webrepl_setup"></span>

|    |
| --- |
| <form action="https://docs.micropython.org/en/latest/esp32/quickref.html" method="get" target="_blank"><button type="submit"><mark style="background: Yellow;"><b>MP ESP32 highlight</b></mark></button><input  type="hidden" name="highlight" value="webrepl_setup" /> </form> |

Hile in Micropython hat fehlgeschlagen


[--> Overview](#Overview)
# websocket_helper <span id="websocket_helper"></span>

  * `object <module 'websocket_helper' from 'websocket_helper.py'> is of type module`
  * `hashlib -- <module 'uhashlib'>`
  * `binascii -- <module 'ubinascii'>`
  * `__name__ -- websocket_helper`
  * `__file__ -- websocket_helper.py`
  * `sys -- <module 'sys'>`
  * `DEBUG -- 0`
  * `server_handshake -- <function server_handshake at 0x3ffeea90>`
  * `client_handshake -- <function client_handshake at 0x3ffeeaa0>`

[--> Overview](#Overview)
