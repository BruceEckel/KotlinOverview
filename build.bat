call python preprocess.py
call pandoc -t revealjs -V theme=simple -s -o KotlinOverview.html KotlinOverview.md
call python postprocess.py
call KotlinOverview.html

@rem You can use -V theme=$theme to set your theme as $theme, with the following options:
@rem sky
@rem simple
@rem moon
@rem night
@rem serif

@rem solarized
@rem beige
@rem black
@rem blood
@rem league
@rem white
