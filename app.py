with st.spinner("2. SWI-Prolog rechnet deontische Inferenz durch..."):
                    # Instanziere Prolog sauber pro Durchlauf
                    for fact in extracted_facts:
                        try:
                            # Sicheres Einfügen der NLU-Fakten
                            prolog.assertz(fact)
                        except Exception as e:
                            pass
                    
                    verbote, gebote, erlaubnisse = [], [], []
                    
                    # Explizite Abfrage der Deontik-Regeln
                    try:
                        res_v = list(prolog.query("untersagt(X, Y)"))
                        for item in res_v:
                            verbote.append({"X": str(item["X"]), "Action": str(item["Y"])})
                    except Exception:
                        pass

                    try:
                        res_g = list(prolog.query("gebietet(X, Y)"))
                        for item in res_g:
                            gebote.append({"X": str(item["X"]), "Action": str(item["Y"])})
                    except Exception:
                        pass

                    try:
                        res_e = list(prolog.query("gestattet(X, Y)"))
                        for item in res_e:
                            erlaubnisse.append({"X": str(item["X"]), "Action": str(item["Y"])})
                    except Exception:
                        pass
